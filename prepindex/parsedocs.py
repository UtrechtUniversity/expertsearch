# 6000 Raadsbrieven, memo's, 823 memo's
# Zou later kunnen kijken naar    antwoorden SVs / ingekomen stukken, maar laten we snel testen hoe dit werkt
# En dan beslissen: is covid literatuur een betere dataset? Met auteurs als de experts

import xml.etree.ElementTree as ET
import os
import requests
import pdfplumber

documents_dir = "./docs/"

# get list of files
brieven = [s for s in os.listdir("./brieven")]
memos = [s for s in os.listdir("./memos")]


#For each file we'll make a seperate json

for file in brieven:
    tree = ET.parse("./brieven/" + file)
    root = tree.getroot()

    #Parse list_ and report_ files differently
    #Addendum: it seems the reports contain duplicate info, so we'll ignore reports
    if "list_" in file:
        with open(file + '.json', 'a') as jsonfile:
            for entry in root:
                       
                #One entry may have multiple documents (attachments)
                print("Found " + str(len(entry.findall("document"))) + " docs")
                for doc in entry.findall("document"):
                
                    docid = doc.attrib['id'].replace("`", "")
                    #skip doc if we already know it!
                    if os.path.isfile(documents_dir + docid + ".pdf"):
                        continue
                    
                    #get all the info we want to store
                    #doc = [docid, entryid, author, date, beleidsveld, onderwerp, full-text]

                    entryid = entry.attrib['id'].replace("`", "")
                    author = "unparsed".replace("`", "")
                    fulltext = 'unparsed'.replace("`", "")
                    title = doc.find("displayname").text.replace("`", "")
                    
                    #I'm messing up the syntax trying to get the proper attributes.. 
                    #So let's just iterate through the children
                    beleidsveld = ""
                    onderwerp = ""
                    date = ""
                    for prop in entry.findall("property"):
                        if prop.attrib['key'] == "Ontvangstdatum":
                            if(prop.text):
                                date = prop.text.replace("`", "")
                        if prop.attrib['key'] == "Beleidsveld":
                            #if it's not none (old files have no metadata)
                            if(prop.text):
                                beleidsveld = prop.text.replace("`", "")
                        if prop.attrib['key'] == "Onderwerp":
                            if(prop.text):
                                onderwerp = prop.text.replace("`", "")
                    
                    
                    
                    response = requests.get(doc.find("publicdownloadurl").text)
                    docfile = open(documents_dir + docid + ".pdf", "wb")
                    docfile.write(response.content)
                    docfile.close()
                
                    try:
                        jsonfile.write(docid + '`' + title + '`' + entryid + '`' + author + '`' + beleidsveld + '`' + onderwerp + '`' + date + '`' + fulltext + '\n')
                        #sometimes it fails (encoding errors)
                    except:
                        print('ignored one document')
"""                
                
#This is a near exact copypasta of the above - except that an attribute has a different name:   Ontvangstdatum -> Datum invoer 
for file in memos:
    tree = ET.parse("./memos/" + file)
    root = tree.getroot()

    #Parse list_ and report_ files differently
    #Addendum: it seems the reports contain duplicate info, so we'll ignore reports
    if "list_" in file:
        with open(file + '.json', 'w') as jsonfile:
            for entry in root:
                       
                #One entry may have multiple documents (attachments)
                print("Found " + str(len(entry.findall("document"))) + " docs")
                for doc in entry.findall("document"):
                    #get all the info we want to store
                    #doc = [docid, entryid, author, date, beleidsveld, onderwerp, full-text]
                    docid = doc.attrib['id'].replace("`", "")
                    entryid = entry.attrib['id'].replace("`", "")
                    author = "unparsed".replace("`", "")
                    fulltext = 'unparsed'.replace("`", "")
                    title = doc.find("displayname").text.replace("`", "")
                    
                    #I'm messing up the syntax trying to get the proper attributes.. 
                    #So let's just iterate through the children
                    beleidsveld = ""
                    onderwerp = ""
                    for prop in entry.findall("property"):
                        if prop.attrib['key'] == "Datum invoer":
                            date = prop.text.replace("`", "")
                        if prop.attrib['key'] == "Beleidsveld":
                            #if it's not none (old files have no metadata)
                            if(prop.text):
                                beleidsveld = prop.text.replace("`", "")
                        if prop.attrib['key'] == "Onderwerp":
                            if(prop.text):
                                onderwerp = prop.text.replace("`", "")
                    
                    #Testing
                    
                    #print(doc.find("publicdownloadurl").text)
                    #print(docid)
                    #print(entryid)
                    #print(author)
                    #print(beleidsveld)
                    #print(onderwerp)
                    #print(date)
                    #print(fulltext)
                    #print()
                    response = requests.get(doc.find("publicdownloadurl").text)
                    docfile = open(documents_dir + docid + ".pdf", "wb")
                    docfile.write(response.content)
                    docfile.close()
                
                    try:
                        jsonfile.write(docid + '`' + title + '`' + entryid + '`' + author + '`' + beleidsveld + '`' + onderwerp + '`' + date + '`' + fulltext + '\n')
                    except:
                        print('ignored one memo')
                """
                

"""        
    for meeting in root:
        for child in meeting:
            if(child.tag=="document"):
                print(child.find('publicdownloadurl'))
        
        #    print(child.tag)
        if meeting.find("document"):
            for doc in meeting.find("document"):
                print('doc')
                print(doc)
                for child in doc:
                    print(child)
                print(doc.find("publicdownloadurl"))
#        print(meeting.find("publicdownloadurl"))
#        meeting["document id"]
#        meeting["publicdownloadurl"]
"""