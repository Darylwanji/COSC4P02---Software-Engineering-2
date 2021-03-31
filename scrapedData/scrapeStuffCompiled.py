from selenium import webdriver
from bs4 import BeautifulSoup

#Name: Kenny Yang - 5934104
#The following python script will require an installation of both selenium, beautifulsoup4, as well as a ChromeDriver corresponding to its Chrome version installed

#This method is called by providing a beautiful soup element which contains all the information within a web page
#This method stores information within course_title and course_info
# course_title stores the course code
# Within course_info stores information regarding a course

def getCourseInfo(s):
    
    course_title = []
    course_info = []
    
    for a in s.findAll('td', attrs = {'colspan' : '2'}):
        if a.find('p',attrs = {'class':'calcname'}) is not None:
            course_title.append(a.text)
        if a.find('p', attrs = {'class':'calitalic'}) is not None:
            course_info.append(a.text)
    return zip(course_title, course_info)

#This method is called by providing a beautiful soup element which contains all the information within a web page
#This method stores information within page_text
# page_text stores all the unique text on the web page

def getPageText(s):
    
    page_text = []
    for a in s.findAll('div', attrs = {'class':'wpb_wrapper'}):
        
        if a.find('p') is not None:
            aString = str(a.find('p').text)
        
            if aString not in page_text:
                page_text.append(aString)
        
    return page_text

#This method is called by providing a beautiful soup element which contains all the information within a web page
#This method stores information within table1
#A counter is used to separate the two tables as this is a specific method for a single web page
# The elements within table1 are stored in order from left to right 

def getVCTABLE(s):
    
    table1 = []
    
    counter = 1
    
    table1.append(str(counter))
    
    for a in s.findAll('span', attrs = {'class':'vc_table_content'}):
        if a is not None:
            table1.append(a.text)
        if len(table1) == 37:
            table1.append(str(counter + 1))
    return table1

#This method is called by providing a beautiful soup element which contains all the information within a web page
#This method stores information within listStuff
# listStuff stores tables within the web pages
#  an integer of the titles of columns is first stored
#  corresponding data is then stored

def getGSHEETS(s):
    
    listStuff = []
    
    for a in s.findAll('div',attrs = {'class':'gsheets-table-container'}):
        
        page_text = []
        
        for b in a.findAll('th'):
            if b.has_attr('data-sort'):
                
                if b is not None:
                    
                    page_text.append(b.text)
                    
        if len(page_text) > 0:
            listStuff.append(str(len(page_text)))
            
        for b in page_text:
            listStuff.append(b)
        
        for b in a.findAll('td'):
            if b.has_attr('style'):
                listStuff.append(b.text)
                  
    return listStuff

#This method is called by providing a beautiful soup element which contains all the information within a web page
#This method stores information within info
# A # signifies the start and end of a section (wpb_wrapper)
# Information pertaining to the title is also saved

def getVCTTA(s):
    
    info = []
    
    for a in s.findAll('div', attrs = {'class':'vc_tta-panel'}):
        title = str(a.find('span', attrs = {'class':'vc_tta-title-text'}).text)
        if title not in info:
            info.append('#')
            info.append(title)
        
        aString = []
        bString = ''
        
        for b in a.findAll('div', attrs = {'class':'wpb_wrapper'}):
            for c in b.findAll('p'):
                if str(c.text) is not None:
                    if str(c.text) not in aString:
                        aString.append(str(c.text))
                
                for d in c.findAll('span', attrs = {'data-contrast':'auto'}):
                    if str(d.text) is not None:
                        if str(d.text) not in aString:
                            aString.append(str(d.text))
                aString.append('SPLIT')
            for c in b.findAll('li'):
                if c is not None:
                    if str(c.text) not in aString:
                        aString.append(str(c.text))
                aString.append('SPLIT')
        for b in aString:
            if b is not None:
                bString += b + ' '
        
        cString = bString.encode('ascii', errors = 'ignore').decode('ascii').split('SPLIT')
        
        for b in cString:
            
            hold = b.rstrip()
            hold2 = str(hold.lstrip())
            
            if any(hold2 in c for c in info):
                pass
            else:
                if hold2 != '':
                    if hold2 != '\n':
                        if len(hold2) <= 1:
                            if hold2 != '#':
                                pass
                        else:
                            info.append(hold2)
            
    return info

#This method is called by providing a beautiful soup element which contains all the information within a web page
#This method stores information within page_text
# A variable, endList, is set to indicate the start and end of a list
# Information pertaining to the web page is scraped into page_text
# If a string ends with : a list of items is assumed to follow
#  The list of information is then combined with the string containing : as the lead and its content under it
#  endList is set to true and $ is appended to indicate the start and end of a list

def getAltPageText(s):
    
    page_text = []
    save = ''
    endList = False
    
    for a in s.findAll('div', attrs = {'class':'wpb_wrapper'}):
        
        for b in a.findAll('p'):
            if b is not None:
                aString = str(b.text.rstrip())
                
                if aString not in page_text:
                    
                    if len(aString) >= 1:
                        if aString[len(aString) - 1] == ':':
                            save = aString
                            pass
                        else:
                            page_text.append(aString)
                    
        if save != '':
            if str(save) not in page_text:
                
                endList = True
                page_text.append('$')
                page_text.append(str(save))
        
        for b in a.findAll('li'):
            if b is not None:
                aString = str(b.text)
                
                if aString not in page_text:
                    page_text.append(aString)
                    
        if endList == True:
            endList = False
            page_text.append('$')
    return page_text

#This method scrapes through all web pages provided through a text document
#This method separates the scraped information of web pages using a new line followed by an integer value followed by another new line
#This method formats a web pages' information as followed:
# The Course Field title
# A string or two providing further information regarding the courses
# A pattern of specific courses then begin
#  A Course Code of length at most 10 with a space at either the 4th or 5th position
#  A course title that pertains to the specific course followed by a few lines that also pertain to that specific course
# The end of the courses provided is provided by an Administrative Assistant which is followed by the Administrative Assistant's name, their contact information, their office location and then a contact email
# The following lines before the blank line indicating another web page further provide more information of the courses

def scrape1():
     
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
    driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')
    
    f = open("scrapestuff.txt","r")
    f1 = open("scrapeInfo.txt","w+")
    count = 1

    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        f1.write("\n%d\r\n" % (count))
        
        stuff = getCourseInfo(soup)
        
        title = soup.find('a',attrs = {'name':'sec1'})
        if title is not None:
            f1.write(title.text)
            f1.write('\n')
        
        for row in stuff:
            for val in row:
                hold = val.split('\n')
                
                for i in range(len(hold)):
                    
                    if hold[i] != '':
                        source = hold[i].encode('ascii', errors = 'ignore').decode('ascii')
                        f1.write(str(source))
                        f1.write('\n')
        count += 1
        
    f.close()
    f1.close()
    driver.close()

#This method scrapes through all web pages provided through a text document
#This method separates the scraped information of web pages using a new line followed by an integer value followed by another new line
#This method formats a web pages' information as followed:
# The title of the web page
# Information regarding the title
#The information regarding the title is all stored within a long string if the information was a paragraph and so splitting the long paragraphs by (., ?, !) is possible

def scrape2():
    
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')
    
    f = open("scrapestuff2.txt","r")
    f1 = open("scrapeInfo2.txt","w+")
    count = 1

    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        f1.write("\n%d\r\n" % (count))
        
        stuff = getPageText(soup)
        
        title = soup.find('title')
        if title is not None:
            f1.write(title.text)
            f1.write('\n')
        
        for row in stuff:
            
            hold = row.split('\n')
            
            for i in range(len(hold)):
                
                if hold[i] != '':
                    f1.write(str(hold[i]))
            f1.write('\n')
            
        count += 1
        
    f.close()
    f1.close()
    driver.close()
    
#This method scrapes through all web pages provided through a text document
#As this method only works in regards to a specific web page the formatting will be specific to this web page
#This method formats a web pages' information as followed:
# The title of the web page
# An integer value which tells the beginning of a table
# As there are only 3 fields, the next 3 lines will be slotted into their corresponding field
#  if a field is empty it means that it corresponds to the last non-empty field in its column

def scrape3():
    
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
    driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')

    f = open("scrapestuff3.txt","r")
    f1 = open("scrapeInfo3.txt","w+")
    
    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        stuff = getVCTABLE(soup)
        
        title = soup.find('title')
        if title is not None:
            f1.write(title.text)
            f1.write('\n')
        
        for row in stuff:
            f1.write(row)
            f1.write('\n')
            
    f.close()
    f1.close()
    driver.close()
    
#This method scrapes through all web pages provided through a text document
#This method separates the scraped information of web pages using a new line followed by an integer value followed by another new line
#This method formats a web pages' information as followed:
# The title of the web page
# A single integer n indicates the start of a table
#  The following n values will be stored as the title of a column
#  The following n*m values will be stored corresponding to their column
# The table ends at either a blank new line, which indicates the end of the web page, or another integer, which indicates the start of a new table

def scrape4():
    
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
    driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')
    
    f = open("scrapestuff4.txt","r")
    f1 = open("scrapeInfo4.txt","w+")
    count = 1
    
    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
    
        f1.write("\n%d\r\n" % (count))
        
        stuff = getGSHEETS(soup)
        
        title = soup.find('title')
        if title is not None:
            f1.write(title.text)
            f1.write('\n')
        
        for row in stuff:
            f1.write(row)
            f1.write('\n')
            
        count+= 1
    
    f.close()
    f1.close()
    driver.close()
    
#This method scrapes through all web pages provided through a text document
#This method separates the scraped information of web pages using a new line followed by an integer value followed by another new line
#This method formats a web pages' information as followed:
# The title of the web page
# A # sign indicates the start of a table
#  The first line represents the title of the table
#  The following lines don't follow strict rules as they are information pertaining to the title
# A blank new line followed by the corresponding integer value indicates the end of a web page, otherwise it is skipped over

def scrape5():
    
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
    driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')
    
    f = open("scrapestuff5.txt","r")
    f1 = open("scrapeInfo5.txt","w+")
    count = 1   
    
    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        f1.write("\n%d\r\n" % (count))
        
        stuff = getVCTTA(soup)
        
        title = soup.find('title')
        if title is not None:
            f1.write(title.text)
            f1.write('\n')
        
        for row in stuff:
            
            hold = row.encode('ascii', errors = 'ignore').decode('ascii')
            
            if len(hold) > 0:
                f1.write(row.encode('ascii', errors = 'ignore').decode('ascii'))
                f1.write('\n')
            
        count+= 1
    
    f.close()
    f1.close()
    driver.close() 
    
#This method scrapes through all web pages provided through a text document
#This method separates the scraped information of web pages using a new line followed by an integer value followed by another new line
#This method formats a web pages' information as followed:
# The title of the web page
# Information pertaining to the web page
# A $ indicates the start of a list
#  The first string after the $ indicates the topic
#  The following strings will be bullet points pertaining to the topic
# Another $ will indicate the end of a list, if a list only has one element (topic) then the last character of the string will be changed from : -> .

def scrape6(): 
    
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
    driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')
    
    f = open("scrapestuff6.txt","r")
    f1 = open("scrapeInfo6.txt","w+")
    count = 1   
    
    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        f1.write("\n%d\r\n" % (count))
        
        stuff = getAltPageText(soup)
        
        title = soup.find('title')
        if title is not None:
            f1.write(title.text)
            f1.write('\n')
        for row in stuff:
            
            f1.write((row.lstrip()).encode('ascii', errors = 'ignore').decode('ascii'))
            f1.write('\n')
            
        count += 1
    
    f.close()
    f1.close()
    driver.close() 

def main():
    scrape1()
    scrape2()
    scrape3()
    scrape4()
    scrape5()
    scrape6()

main()