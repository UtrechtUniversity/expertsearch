#After downloading the documents and parsing metadata,
#we read add the fulltext and experts to that metadata

#Author extraction mostly goes wrong when there's multiple authors (if text > 30, thenw e assume something went wrong)
import json
import pdfplumber

parsed_files = ['list_41b35454-6329-4f11-b803-d7e5a6141085-13.xml', 'list_ac711b72-54f7-449a-9a73-9693e6e06688.xml.json']
unread = 0

#we split up the parsing into parts to avoid technical issues
part = 0
part_counter = 0
part_limit = 100

for file in parsed_files:
    #new empty json to store it in
    data = {}
    with open(file) as current_file:
        for line in current_file.readlines():
            pieces = line.split('`')
            #jsonfile.write(docid + '`' + title + '`' + entryid + '`' + author + '`' + beleidsveld + '`' + onderwerp + '`' + date + '`' + fulltext + '\n')
            #print(pieces)
            
            #Now open the relevant doc
            text = ""
            try:
                with pdfplumber.open("./docs/"+pieces[0]+".pdf") as pdf:
                    # loop through the pages and add the text of each page to the overall text of the pdf
                    for page in pdf.pages:
                        try:
                            text = text + page.extract_text()
                        except:
                            continue
            except:
                print("could not read file ./docs/"+pieces[0]+".pdf")
                unread += 1

            #On the first page we look for the author by looking for the text between start and end
            p1 = pdf.pages[0].extract_text()
            start = "Behandeld door"
            start2 = "Behandeld" #if the first fails, we try an edge case
            end = "Datum"

            #print(p1)
            #print('result')
            if not p1:
                result = 'Unknown / parsing error'
            else:
                result = p1[p1.find(start)+len(start):p1.rfind(end)]
                #probably got something wrong
                if len(result) > 30 or len(result) < 4:
                    result = p1[p1.find(start2)+len(start2):p1.rfind(end)]
                    #If the result still doesn't make sense, we didn't find it
                    if len(result) > 20 or len(result) < 4:
                        result = 'Unknown for ' + pieces[1] + ' ' + pieces[0]
                        #print('Mistake?')
            print (result.strip())

            # save the text and author of the pdf file
            
            data[pieces[0]] = {
                'docid': pieces[0],
                'title': pieces[1],
                'entryid': pieces[2],
                'author': result.strip(),
                'beleidsveld': pieces[4],
                'onderwerp': pieces[5],
                'date': pieces[6],
                'fulltext': text,
            }
            
            part_counter += 1
            if(part_counter == part_limit):
                
                #Now store the results for this part
                with open('results-' + str(file) + str(part) + '.json', 'w') as fp:
                    json.dump(data, fp)
                    
                data = {}
                
                part_counter = 0
                part += 1

    #Now store the remaining results for this file
    with open('results-' + str(file) + str(part + 1) + '.json', 'w') as fp:
        json.dump(data, fp)
    
        
print("could not read this many: " + unread)
        
#Notes for expert extraction
    #Behandeld door (Tabs) naam         file:///C:/Users/tmsch/Downloads/Memo%20Domplein_%20digitale%20handhaving%20(2).pdf
    #