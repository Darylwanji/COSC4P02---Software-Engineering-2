from bs4 import BeautifulSoup
import urllib

#Those two methods are called by providing a beautiful soup element which contains all the information within a web page
#Those two methods store information within page_title
# page_title stores the website title
def getGenInfo_Brock(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    page_title = soup.title.text
    f1.write(str(page_title)+'\r')

def getGenInfo_Niagara(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    page_title = soup.title.text
    f1.write(str(page_title)+'\r')
    
f_brock = open('directLink_brock.txt','r')
f_niagara = open('directLink_niagara.txt','r')
f1 = open('resultText.txt','a')

#Those two methods scrape through all web pages provided through a text document
#Those two methods separate the scraped information of web pages using a new line
#Those two methods print the number to indicate the order and the website title with it's address
def scrap_brock():
    count = 1
    for i in f_brock:
        link = urllib.request.urlopen(i)
        html_text = link.read()
        f1.write(str(count))
        f1.write("\r")
        getGenInfo_Brock(html_text)
        f1.write(i)
        f1.write("\r\n")        
        count += 1

def scrap_niagara():
    count_ = 12
    for i in f_niagara:
        link = urllib.request.urlopen(i)
        html_text = link.read()
        f1.write(str(count_))
        f1.write("\r")
        getGenInfo_Niagara(html_text)
        f1.write(i)
        f1.write("\r\n") 
        count_ += 1        

#Call the main method to run the program        
def main():
   scrap_brock()
   f1.write("\r\n")
   scrap_niagara()
                   
if __name__ == "__main__":
    main()
    
