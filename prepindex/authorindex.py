import json
import os

#for testing
#files = ['results-list_41b35454-6329-4f11-b803-d7e5a6141085-10.xml0.json']
files = [s for s in os.listdir("./json")]


indexed_count = 0
skipped_count = 0

authors = {}
#authors can write their names in different ways (usually with initials or full)
#keep track of them
duplicates = {}

#add document for this author
def addauthor(authors, author, doc, file, data):
    if author in authors:
        authors[author].append((doc, file, data[doc]['beleidsveld'], data[doc]['onderwerp']))
    else:
        authors[author] = [(doc, file, data[doc]['beleidsveld'], data[doc]['onderwerp'])]

for file in files:
    #not sure why json.load failed.. we just do it this way instead
    data = json.loads(open('./json/' + file).readlines()[0])
    for doc in data:
        author = data[doc]['author']
        #print(data[doc]['author'])
        #print(author)
        #print(doc)
        #print(file)
        
        #if the author and fulltext are known, parse this result
        if data[doc]['fulltext'] != 'unparsed' and author != 'unparsed' and \
                    not ('nknown' in author):

            #if this is the mistake where some 'authors' are parsed wrong
            if(author[-3:-1] == "20"):
                continue
            #if we parsed a word instead of author name
            if(len(author.split(" ")) < 2):
                continue
            #if there are multiple authors
            if('/' in author or ' - ' in author or '&' in author):
                continue
#                aa = author.split('/')
#                for a in aa:
#                    addauthor(authors, a.strip(), doc, file, data)
#                    indexed_count += 1
            elif(' en ' in author):
                continue
 #               aa = author.split(' en ')
 #               for a in aa:
 #                   addauthor(authors, a.strip(), doc, file, data)
 #                   indexed_count += 1
            elif(', ' in author):
                continue
            #normal case
            else:
                addauthor(authors, author, doc, file, data)
                indexed_count += 1
            
        else:
            skipped_count += 1

#test results
"""
for index, author in enumerate(authors):
    print(author)
    print(authors[author])
    if(index > 5):
        break
"""



#Let's analyze the results
#print(indexed_count)
#print(skipped_count)

#How many authors?
#print(len(authors))
authlen = len(authors)

#Let's group authors on last name, to see if we have many synonyms
lastnames = {}
for author in authors:
    lastname = author.split(" ")[-1]
    if lastname in lastnames:
        lastnames[lastname].append(author)
    else:
        lastnames[lastname] = [author]
        
#print(len(lastnames))


#if a name starts with mr. Mr. or Mr we want to remove that for comparing first names
#only occurs for 9 names
def removeTitle(name):
    if name[:3] == "Mr." or name[:3] == "mr." or name[:3] == "Mw." or name[:3] == "mw.":
        return name[3:].strip()
    if name[:2] == "mw" or name[:2] == "mr":
        return name[2:].strip()
    return name

#Let's investigate manually

#We see a few use cases
    # First letter first name and last name matches -> same author
    # First name is substring of second name -> two authors
        # -> fixed
    # Different authors
        # -> correct
    
    # mistakes that end in '201' (a year)
        # -> fixed during building index
#This approach ignores two authors case -> assumes only last author 
    # Can recognize two authors by '/' or ' en '
        # In this case we should assign the doc to both sub authors
        # -> fixed during building of author index
for lastname in lastnames:
    if(len(lastnames[lastname]) > 1):
        
        #if we find a duplicate author, merge documents
        #create a set of these authors that we can change
        todoset = list(lastnames[lastname])
        #while the set is not empty
        while todoset:
            #print(todoset)
            #take the first name
            curname = todoset[0]
            i = 1
            for j in range(1, len(todoset)):
                #print('comparing')
                #print(curname)
                #print(todoset[i])

                #if the first letter of both names matches
                #edge cases
                    #name starts with 'mr. ' 'Mr '
                if removeTitle(todoset[i])[0] == removeTitle(curname)[0]:
                    #print('removing')
                    
                    # add the docs of 
                    test = authors.pop(todoset[i])
                    
                    #remember this duplcicate name!
                    if curname in duplicates:
                        duplicates[curname].append(todoset[i])
                    else:
                        duplicates[curname] = [todoset[i]]
                    
                    #print(test)
                    authors[curname].extend(test)
                    #print(authors[curname])
                    
                    #remove the new author from the working set, adjust the index for the loop
                    todoset.pop(i)
                else:
                    i += 1
                  
            #remove current item
            todoset.pop(0)
            
print('After deduplicating ' + str(authlen) + ' authors, we have ' + str(len(authors)))

#Now re-add duplicate names so that we still recognize them
#EDIT: skip this! because then the same author will be indexed twice. we should store the duplciates instead
#for author in duplicates:
#    #all duplicate names for this author
#    for dupe in duplicates[author]:
#        #copy same as original has
#        authors[dupe] = list(authors[author])
        
print(len(duplicates))
print(len(authors))
        
#store experts info for future ref
with open('experts.json', 'w') as fp:
    json.dump(authors, fp)

with open('duplicates.json', 'w') as fp:
    json.dump(duplicates, fp)
