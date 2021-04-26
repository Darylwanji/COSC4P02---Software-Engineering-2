from selenium import webdriver
from bs4 import BeautifulSoup

course_code = []
course_time = []

excludeSwitches: ['enable-logging']

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options = options,executable_path='chromedriver_win32/chromedriver')
driver.get('https://brocku.ca/webcal/2021/undergrad/btec.html')

content = driver.page_source
soup = BeautifulSoup(content,'html.parser')

#print(soup)

for a in soup.findAll('td', attrs = {'colspan' : '2'}):
    
    if a.find('p', attrs = {'class' : 'calccode'}) is not None:
        code = a
        course_code.append(code.text)
        name = a.find('p', attrs = {'class' : 'calcname'})
        if a.find('p', attrs = {'class' : 'calitalic'}) is not None:
            time = a
            course_time.append(time.text)
        

for (a,b) in zip(course_code, course_time):
    print(a)
    #print(b)