from selenium import webdriver
from bs4 import BeautifulSoup
from test.datetimetester import OTHERSTUFF

def getCourseInfo(s):
    
    course_title = []
    course_info = []
    
    for a in s.findAll('td', attrs = {'colspan' : '2'}):
        if a.find('p',attrs = {'class':'calcname'}) is not None:
            course_title.append(a.text)
        if a.find('p', attrs = {'class':'calitalic'}) is not None:
            course_info.append(a.text)
    return zip(course_title, course_info)

def getPageText(s):
    page_text = []
    for a in s.findAll('div', attrs = {'class':'wpb_wrapper'}):
        
        if a.find('p') is not None:
            aString = str(a.find('p').text)
        
            if aString not in page_text:
                page_text.append(aString)
        
    return page_text

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

def scrape1():
    f = open("scrapestuff.txt","r")
    f1 = open("scrapeInfo.txt","w+")
    count = 1

    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        f1.write("\n%d\r\n" % (count))
        
        stuff = getCourseInfo(soup)
        
        for row in stuff:
            for val in row:
                hold = val.split('\n')
                
                for i in range(len(hold)):
                    
                    if hold[i] != '':
                        source = hold[i].encode("utf-8")
                        f1.write(str(source))
                        f1.write('\n')
        count += 1
    f.close()
    f1.close()

def scrape2():
    f = open("scrapestuff2.txt","r")
    f1 = open("scrapeInfo2.txt","w+")
    count = 1

    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        f1.write("\n%d\r\n" % (count))
        
        stuff = getPageText(soup)
        
        for row in stuff:
            
            hold = row.split('\n')
            
            for i in range(len(hold)):
                
                if hold[i] != '':
                    f1.write(str(hold[i]))
            f1.write('\n')
            
        count += 1
    f.close()
    f1.close()

def scrape3():
    
    f = open("scrapestuff3.txt","r")
    f1 = open("scrapeInfo3.txt","w+")
    
    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
        
        stuff = getVCTABLE(soup)
        
        for row in stuff:
            f1.write(row)
            f1.write('\n')

def scrape4():
    f = open("scrapestuff4.txt","r")
    f1 = open("scrapeInfo4.txt","w+")
    count = 1
    
    for x in f:
        driver.get(x)
        content = driver.page_source
        soup = BeautifulSoup(content,'html.parser')
    
        f1.write("\n%d\r\n" % (count))
        
        stuff = getGSHEETS(soup)
        
        for row in stuff:
            f1.write(row)
            f1.write('\n')
            
            count+= 1

def main():
    scrape1()
    scrape2()
    scrape3()
    scrape4()

excludeSwitches: ['enable-logging']
    
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')
    
main()


driver.close()
