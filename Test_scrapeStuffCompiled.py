import unittest
from selenium import webdriver
import scrapeStuffCompiled as case
from bs4 import BeautifulSoup


class Test_scrapeStuffCompiled(unittest.TestCase):

    def setUp(self):
        print("Before each use case is executed, the setUp method is called to prepare the environment")
        print("\r\n")

    def tearDown(self):
        print("After each use case is executed, the tearDown method is called to clean up the environment")
        print("\r\n")
        
    def test_getCourseInfo(self):
        print('test getCourseInfo')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        f = open("scrapestuff.txt","r")
        for x in f:
            driver.get(x)
            content = driver.page_source
            soup = BeautifulSoup(content,'html.parser')
   
        self.assertIsNotNone(case.getCourseInfo(soup))
    
    def test_getPageText(self):
        print('test getPageText')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        f = open("scrapestuff2.txt","r")
        for x in f:
            driver.get(x)
            content = driver.page_source
            soup = BeautifulSoup(content,'html.parser')
   
        self.assertIsNotNone(case.getPageText(soup))

        
    def test_getVCTABLE(self):
        print('test getVCTABLEt')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        f = open("scrapestuff3.txt","r")
        for x in f:
            driver.get(x)
            content = driver.page_source
            soup = BeautifulSoup(content,'html.parser')
   
        self.assertIsNotNone(case.getVCTABLE(soup))
    
    def test_getGSHEETS(self):
        print('test getGSHEETS')
        print("\r\n")
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        f = open("scrapestuff4.txt","r")
        for x in f:
            driver.get(x)
            content = driver.page_source
            soup = BeautifulSoup(content,'html.parser')
   
        self.assertIsNotNone(case.getGSHEETS(soup))
        
    def test_getVCTTA(self):
        print('test getVCTTA')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        f = open("scrapestuff5.txt","r")
        for x in f:
            driver.get(x)
            content = driver.page_source
            soup = BeautifulSoup(content,'html.parser')
   
        self.assertIsNotNone(case.getVCTTA(soup))
    
    def test_getAltPageText(self):
        print('test getVCTTA')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        f = open("scrapestuff6.txt","r")
        for x in f:
            driver.get(x)
            content = driver.page_source
            soup = BeautifulSoup(content,'html.parser')
   
        self.assertIsNotNone(case.getAltPageText(soup))      

    
    
if __name__ == '__main__':
    unittest.main()