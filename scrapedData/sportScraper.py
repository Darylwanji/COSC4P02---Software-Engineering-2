# importing the libraries
from bs4 import BeautifulSoup
import requests
import json
#Santiago Franco

#The scraper takes in the links  of each sport from a text file and parses the HTML for each creating a JSON file storing the necessary data

#The JSON format is a list of each sport
#[sports
#  {
#   sportname,
#   generalinfo,
#   table1,
#   table2,
#   table3,
#   alumni },]
#Each table withing the sport object has nested values which are Title and header,row1 - row8 which are a list of values
#alumni has 3 dictionaries nested within which each have a name and link value

#parses and gets the general info of each sport and returns it as a string
def getGenInfo(html_content):
    soup = BeautifulSoup(html_content, "lxml")

    general = soup.find('div',{"class":"rich-text-block-4 w-richtext"})

    generalInfo = ''
    # for each block of text in the general section add it to the general info string
    for i in general:
        if str(i.text) != "General Description":
            generalInfo += str(i.text).replace(u'Â', u' ')
  
    return str(generalInfo.encode('ascii', 'ignore').decode("utf-8"))

#receives name of table and parses all tbale data into seperate rows assigning them into a dict for return
def getTableData(html_content,tablenum):
    soup = BeautifulSoup(html_content, "lxml")
    general = soup.find('div',{"class":tablenum})

    #init counter to keep track of curr row
    count = 1
    header = []


    #init row lists
    row1, row2, row3, row4, row5, row6, row7, row8 = ([] for i in range(8))

    #if count is 1 then its the title if less than or equal to 6 then those are the headers
    for i in general:
        if count == 1:
            title = str(i.text)
            count+=1
        elif count <= 6:
            header.append(str(i.text))
            count +=1
    #for every 5 items assign them to a row and then move on to next row
        #row1
        elif count <= 11:
            if str(i.text):
                row1.append(str(i.text))
            else:
                row1.append(str("NA"))
            count+=1

        #row2
        elif count <= 16:
            if str(i.text):
                row2.append(str(i.text))
            else:
                row2.append(str("NA"))
            count+=1

        #row3
        elif count <= 21:
            if str(i.text):
                row3.append(str(i.text))
            else:
                row3.append(str("NA"))
            count+=1


        #row4
        elif count <= 26:
            if str(i.text):
                row4.append(str(i.text))
            else:
                row4.append(str("NA"))
            count+=1


        #row5
        elif count <= 31:
            if str(i.text):
                row5.append(str(i.text))
            else:
                row5.append(str("NA"))
            count+=1


        #row6
        elif count <= 36:
            if str(i.text):
                row6.append(str(i.text))
            else:
                row6.append(str("NA"))
            count+=1


        #row7
        elif count <= 41:
            if str(i.text):
                row7.append(str(i.text))
            else:
                row7.append(str("NA")) 
            count+=1 


        #row8
        elif count <= 46:
            if str(i.text):
                row8.append(str(i.text))
            else:
                row8.append(str("NA"))
            count+=1 
    table = {
        "Title":title,
        "Header":header,
        "row1":row1,
        "row2":row2,
        "row3":row3,
        "row4":row4,
        "row5":row5,
        "row6":row6,
        "row7":row7,
        "row8":row8
    }
     

   
    return table

#parses and gets the names of each notable alumni and the links to their profile page
def getAlumni(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    al = soup.find('div',{"class":"section-9"})

    #init data and alumni name and link variables
    data = []
    a1, a2, a3 = ({} for i in range(3))
    a1link,a1name,a2link,a2name,a3link,a3name =('' for i in range(6))
    #init count
    count = 0

    #gets each item in the alumni section and if a link or name set it to the appropriate variable depending on which alumni it is, keeping tracking using count
    for i in al:
        if i.has_attr('href'):
            count+=1
            if count <=2:
                a1link = str(i['href'].encode('ascii', 'ignore').decode("utf-8"))
            elif count <=4:
                a2link = str(i['href'].encode('ascii', 'ignore').decode("utf-8"))
            elif count <=6:
                a3link = str(i['href'].encode('ascii', 'ignore').decode("utf-8"))
          
           
        if i.find('div',{"class":"text-block-32"}):
            count+=1
            if count <=2:
                a1name = str(i.text.encode('ascii', 'ignore').decode("utf-8"))
            elif count<=4:
                a2name = str(i.text.encode('ascii', 'ignore').decode("utf-8"))
            elif count<=6:
                a3name = str(i.text.encode('ascii', 'ignore').decode("utf-8"))
           
    
    #create alumni dictionary objects and append it to the data list
    a1 = {
        "name":a1name,
        "link":a1link
    }
    data.append(a1)

    a2 = {
        "name":a2name,
        "link":a2link
    }
    data.append(a2)

    a3 = {
        "name":a3name,
        "link":a3link
    }
    data.append(a3)
    #return data list
    return data


#opem input string to access URL's
f = open('sportScraper.txt','r')

#init data dictionary with a list of sports
data = {}
data['sports'] = []

for url in f:
    # Make a GET request to fetch the raw HTML content
    html= requests.get(str(url))
    html.encoding = html.apparent_encoding
    html_content = html.text

    #get sportname from the url
    sporturl = url.split("/")
    sportname = sporturl[len(sporturl)-1]
   
    #request the general info, table data, and alumni data and set them to variables
    gen = getGenInfo(html_content)
    t1 = getTableData(html_content,"first-table")
    t2 = getTableData(html_content,"second-table")
    t3 = getTableData(html_content,"third-table")
    alumn = getAlumni(html_content)

    #create a dict of the current sports info and append it to the output data
    data['sports'].append({
        'sportname': sportname,
        'generalinfo': gen,
        'table1': t1,
        'table2': t2,
        'table3': t3,
        'alumni':alumn
    })

#writre the final output data to a file as a JSON 
with open('sportInfo.txt','a') as outfile:
    json.dump(data,outfile,indent=4)
    # count += 1
# with open('sportInfo.txt') as json_file:
#     data = json.load(json_file)
#     for s in data['sports']:
#         print(s['table1'])
