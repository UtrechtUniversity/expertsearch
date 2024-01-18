# pre: read documents into docs.json

# using the docs.json, we use the python bulk helper to index these files in elastic
# https://elasticsearch-py.readthedocs.io/en/master/helpers.html

# Windows install: first install and start elastic (bin/elastic.bat)
# Also pip install elasticsearch (for the python libraries), and bigjson
# Get docs.json from the spider, and then do this. Note: I hardcoded a link that should be changed



# deprecated:
# The elastic bulk API wants a certain format, so we prepare 
# the data for that: 1 line says the elastic operation (index),
# the next says the webpage we index
# https://www.elastic.co/guide/en/elasticsearch/reference/7.4/docs-bulk.html
# It also complained about some chars in html (such as parentheses), so I just strip those for now

import os
import sys
import re 
#import bigjson
from urllib.parse import urlparse



#f = open("C:\\Users\\tmsch\\Desktop\\elastic\\docs.json")
#copy = open("C:\\Users\\tmsch\\Desktop\\elastic\\docs2.json","wt")\

# the copying
#for line in f:
#	copy.write("{ \"index\" : { \"_index\" : \"sites\" } }\n")
	#copy.write(strip_tags(line))
#	copy.write(line)
	
#elastic expects a newline at the end
#copy.write("\n")








from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from pathlib import Path
import json
from time import sleep
import unidecode

indexName_doc = 'expert-search-doc-12'
indexName_exp = 'expert-search-exp-13'

#indexFile = 'docs-test.json'
#indexFiles = ['index-test.json']
indexFiles = [s for s in os.listdir("./json")]

print(Path.cwd())


#load expert data
#experts2 has all blacklisted (i.e. non) authors removed 
authors = json.loads(open('experts2.json').readlines()[0])

deleteme = []
#should pre-process experts to make sure we get all aliases
#print(len(authors))
for author in authors:
    name = unidecode.unidecode(author)
    if name != author:
            
        # find alias
        for author2 in authors:
            #compare last names again, and first letters of first name
            if author2.split(" ")[-1] == name.split(" ")[-1] and author2[0] == name[0]:
                print('merging ' + name + ' and ' + author2)
                authors[author2].extend(authors[author])
                found = True
                deleteme.append(author)
                break
            
for a in deleteme:
    authors.pop(a)
    
#print(len(authors))
#This got rid of 6 more doubles!
        
#        if unidecode.unidecode(author) in authors:
#                authors[unidecode.unidecode(author)].merge(a)
            #print('merged ' + author)
#            else:
#            authors[unidecode.unidecode(author)] = a
            #print('renamed ' + author)
    
        

duplicates = json.loads(open('duplicates.json').readlines()[0])

#function to get beleidsvelden for an expert
def getExpertise(author):
    expertises = []
    
    for d in authors[author]:
        if len(d[2]) > 1:
            expertises.append(d[2])
            
    expertises = set(expertises)
    expertise = ""
    for e in expertises:
        if(len(expertise) > 1):
            expertise += ", "
        expertise += e
    return expertise
 
#find unambigiuous name of an author
def realname(author):
    author = unidecode.unidecode(author)
    if author in authors:
        return author
    for a in duplicates:
        if author in duplicates[a]:
            return a
    #else:
    #    print('did not find author ' + author)
 
#Testing  stuff
#for author in authors:
#    print(getExpertise(author))
#    print()
    
#with open(indexFiles[0]) as open_file:
#    data = json.load(open_file)
#    for item in data:
        #print('author ' + data[item]['author'])
#        realname(data[item]['author'])
        #print()

#connect to ES
es = Elasticsearch(timeout=30, max_retries=10, retry_on_timeout=True)




indexed_ids = []

#Data generation for the document-based index
def gendata_doc():
    indexed = 0 #number of files indexed
    parsed = 0
    dupes = 0
    
    for indexFile in indexFiles:
        with open(indexFile) as open_file:
            data = json.load(open_file)
            
            for item in data:
                #IF EXPERT AND FULLTEXT BOTH PARSED AND KNOWN
                #print(data[item])
                if data[item]['fulltext'] != 'unparsed' and data[item]['author'] != 'unparsed' and \
                    not ('nknown' in data[item]['author']):
    
                    auth = realname(data[item]['author'])
                    
                    if data[item]['docid'] not in indexed_ids:

                        #ignore docs in the edge case of a double author
                        if auth in authors:    
                            yield {
                                "_index": indexName_doc,
                                "_type":"document",
                                "_source": {
                                    'docid' : data[item]['docid'],
                                    'title': data[item]['title'],
                                    'entryid': data[item]['entryid'],
                                    'author': auth,
                                    'expertises': getExpertise(auth),
                                    'beleidsveld': data[item]['beleidsveld'],
                                    'onderwerp': data[item]['onderwerp'],
                                    'date': data[item]['date'],
                                    'fulltext': data[item]['fulltext'],
                                }
                            }
                            indexed += 1
                            indexed_ids.append(data[item]['docid'])
                        else:
                            dupes += 1
                parsed += 1
    print(indexed)
    print(parsed)
    print(dupes)
    


es.indices.create(index=indexName_doc, ignore=400)
#perform bulk index
bulk(es, gendata_doc())



# Now do the expertise index 
def gendata_exp():
    indexed = 0 #number of files indexed
    parsed = 0
    
    #we index by author
    for author in authors:
        #get fulltext of all stuff they done wroted
        alltext = ""
        for doc in authors[author]:
            #doc = [docid, jsonid, beleidsveld, onderwerp]
            jsontext = json.loads(open('./json/' + doc[1]).readlines()[0])
            alltext += jsontext[doc[0]]['title'] + " " + jsontext[doc[0]]['fulltext'] + " "
            
        yield {
            "_index": indexName_exp,
            "_type":"document",
            "_source": {
                #'expertid' : data[item]['docid'],         ???
                'author': author,
                'expertises': getExpertise(author),
                'fulltext': alltext,
            }
        }
        indexed += 1
        parsed += 1
    print(indexed)
    print(parsed)


es.indices.create(index=indexName_exp, ignore=400)
#perform bulk index
bulk(es, gendata_exp())
