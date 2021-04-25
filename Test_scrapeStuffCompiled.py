import unittest
from selenium import webdriver
import scrapeStuffCompiled as case
from bs4 import BeautifulSoup
from unittest import TestCase
TestCase.maxDiff = None
from urllib.error import HTTPError
from urllib.error import URLError

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
        try:    
            f = open("scrapestuff.txt","r")
        except OSError:
            print ("Could not open/read file:", f)    
        for x in f:
            driver.get(x)
            content = driver.page_source
            try:
                soup = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")
 
        self.assertIsNotNone(case.getCourseInfo(soup))
      
        
    def test_getPageText(self):
        print('test getPageText')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        try:
            f = open("scrapestuff2.txt","r")
        except OSError:
            print ("Could not open/read file:", f)
            
        for x in f:
            driver.get(x)
            content = driver.page_source
            try:
                soup = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                
                
        self.assertIsNotNone(case.getPageText(soup))
        try:
            f1 = open("scrape_link1.txt","r")
            f2 = open("testResult1.txt","r")
        except OSError:
            print ("Could not open/read file:", f1,f2)            
        p = f2.read()
        for x in f1:
            driver.get(x)
            content = driver.page_source
            try:
                soup1 = BeautifulSoup(content,'html.parser')    
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                
                
        self.assertEqual(str(case.getPageText(soup1)),str(p))
        
    def test_getVCTABLE(self):
        print('test getVCTABLE')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        try:
            f = open("scrapestuff3.txt","r")
            f2 = open("testResult2.txt","r")
        except OSError:
            print ("Could not open/read file:", f,f2)            
        p = f2.read()
        for x in f:
            driver.get(x)
            content = driver.page_source
            try:
                soup = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                
                
        self.assertIsNotNone(case.getVCTABLE(soup))
        self.assertEqual(str(case.getVCTABLE(soup)),str(p))
    
    def test_getGSHEETS(self):
        print('test getGSHEETS')
        print("\r\n")
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        try:
            f = open("scrapestuff4.txt","r")
        except OSError:
            print ("Could not open/read file:", f)
            
        for x in f:
            driver.get(x)
            content = driver.page_source
            try:
                soup = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                           
   
        self.assertIsNotNone(case.getGSHEETS(soup))
        
        try:
            f1 = open("scrape_link2.txt","r")
            f2 = open("testResult3.txt","r")
        except OSError:
            print ("Could not open/read file:", f1,f2)            
                    
        p = f2.read()
        for x in f1:
            driver.get(x)
            content = driver.page_source
            try:
                soup1 = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                
                
        self.assertEqual(str(case.getGSHEETS(soup1)),str(p))
         
    def test_getVCTTA(self):
        print('test getVCTTA')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        try:
            f = open("scrapestuff5.txt","r")
        except OSError:
            print ("Could not open/read file:", f)
            
        for x in f:
            driver.get(x)
            content = driver.page_source
            try:
                soup = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                
                
        self.assertIsNotNone(case.getVCTTA(soup))
    
    def test_getAltPageText(self):
        print('test getAltPageText')
        print("\r\n")        
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver_win32\chromedriver.exe')    
        try:
            f = open("scrapestuff6.txt","r")
        except OSError:
            print ("Could not open/read file:", f)
            
        for x in f:
            driver.get(x)
            content = driver.page_source
            try:
                soup = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                
                
        self.assertIsNotNone(case.getAltPageText(soup))
        
        try:
            f1 = open("scrape_link3.txt","r")
            f2 = open("testResult4.txt","r")
        except OSError:
            print ("Could not open/read file:", f1,f2)
        p = f2.read()
        for x in f1:
            driver.get(x)
            content = driver.page_source
            try:
                soup = BeautifulSoup(content,'html.parser')
            except HTTPError as e:
                print(e)
            except URLError:
                print("Website Can't be reached")                
                
        self.assertEqual(str(case.getAltPageText(soup)),str(p))    

    
    
if __name__ == '__main__':
    unittest.main()