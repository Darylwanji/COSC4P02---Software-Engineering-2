import json
import re

#Name: Kenny Yang - 5934104
#The following python script will only be using json to translate a text document into a json file

def scrapeInfoOneToJson():
    
    #f = open("scrapeInfo.txt","r")
    f = open("scrapeInfo.txt","r")
    
    start = False
    end = False
    sectionStart = False
    courseStart = False
    anAdmin = False
    count = 0
    
    allCourses = []     # Contains a field of study along with courses within that field of study
    oneCourse = {}      # Contains a single field of study's title, courses, descriptions of the field of study, and administrative information
    oneCourse_desc = [] # Contains the descriptions of a field of study
    singleCourse = {}   # Contains all courses offered within a field of study
    singleCourses = []  # Contains a single course within a field of study
    singleCourseInfo = []
    adminInfo = {}
    
    for x in f:
        
        if x == '\n':           # This portion skips the new line
            
            if start == False:
                start = True
                sectionStart = False
            else:
                start = False
                sectionStart = True
            continue
        
        elif start == True:     #This stores information about a course if the title isn't empty
            
            oneCourse = {}      # Contains a single field of study's title, courses, descriptions of the field of study, and administrative information
            oneCourse_desc = [] # Contains the descriptions of a field of study
            singleCourse = {}   # Contains all courses offered within a field of study
            singleCourses = []  # Contains a single course within a field of study
            adminInfo = {}
            anAdmin = False
            count = 0
            
        elif sectionStart == True:
            if not bool(oneCourse):
                                
                y = x.split('\n')
                
                for line in y:
                    if line != '':
                        oneCourse['title'] = line
                        
            elif len(x) <= 17 and len(x) > 6 and anAdmin == False:
                if x[5] == ' ' or x[4] == ' ':
                    
                    if str(x.strip('\n')) == "CO-OP COURSES":
                        continue
                    
                    if str(x.strip('\n'))[0:4] == "Work":
                        
                        singleCourse['course name'] = x[0:len(x)-1]
                        continue
                    
                    if bool(singleCourse):
                        singleCourse['course description'] = singleCourseInfo
                        singleCourses.append(singleCourse)
                        
                    courseStart = True
                    singleCourse = {}
                    singleCourseInfo = []
                    
                    y = x.split('\n')
                    
                    for line in y:
                        s = line.split('#')
                        for aLine in s:
                            if aLine != '':
                                singleCourse['course ID'] = aLine
                else:
                    
                    y = x.split('\n')
                    
                    for line in y:
                        if line != '':
                            singleCourseInfo.append(line)
                    
            elif str(x.strip('\n')) == "Administrative Assistant":
                
                if bool(singleCourse):
                    singleCourse['course description'] = singleCourseInfo
                    singleCourses.append(singleCourse)
                   
                anAdmin = True
                
            elif anAdmin == True:
                count += 1
                
                y = x.split('\n')
                
                for line in y:
                    if line != '':
                        copy = line
                
                if count == 1:
                    adminInfo['admin name'] = copy
                elif count == 2:
                    adminInfo['contact information'] = copy
                elif count == 3:
                    adminInfo['office location'] = copy
                elif count == 4:
                    adminInfo['email'] = copy
                    anAdmin = False
                    courseStart = False
                    oneCourse['Administrative Assistant'] = adminInfo
                    
                    if len(singleCourses) > 0:
                        oneCourse['available courses'] = singleCourses
                        oneCourse['description'] = oneCourse_desc
                        allCourses.append(oneCourse)
                        
                    continue
                
            elif courseStart == False:
                y = x.split('. ')
                
                for line in y:
                    s = line.split('\n')
                    
                    for aLine in s:
                        if aLine != '':
                            oneCourse_desc.append(aLine)
                            
            elif courseStart == True:
                
                y = x.split('\n')
                
                if singleCourse.get('course name') is None:
                    
                    for line in y:
                        if line != '':
                            singleCourse['course name'] = line
                            
                else:
                    for line in y:
                        if line != '':
                            singleCourseInfo.append(line)
    
    json.dump(allCourses,open("scrapeInfoJson.json", "w"), indent = 6)
    
    return allCourses
    
def scrapeInfoTwoToJson():
    
    f = open("scrapeInfo2.txt","r")
    
    start = False
    sectionStart = False
    
    allWebSite = []     #Contains all websites
    oneWebsite = {}     #Contains a website's title + information
            
    title = ''          #Contains the website's title
    info = []           #Contains the website's information in order
 
    for x in f:
        
        if x == '\n':           # This portion skips the new line
           
            if start == False:
                start = True
                sectionStart = False
            else:
                start = False
                sectionStart = True
            continue
        
        elif start == True:     #This stores information about a course if the title isn't empty
            if bool(oneWebsite):
                oneWebsite['description'] = info
                allWebSite.append(oneWebsite)
               
            oneWebsite = {}     #Contains a website's title + information
            
            title = ''          #Contains the website's title
            info = []           #Contains the website's information in order
        
        elif sectionStart == True:
            if title == '':
                title = x[0:len(x) - 1]
                
                y = title.split('\u2013')
                replace = ''
                for line in y:
                    if line[0] == ' ':
                        replace += '-'+line
                    else:
                        replace += line
                
                oneWebsite['title'] = str(replace)
                
            else:
                y = x.split('. ')
                
                for line in y:
                    s = line.split('\n')
                    for aLine in s:
                        
                        s2 = re.split(r'\u2019|\u2018|\u2014|\u2013|\u00a0|\u201c|\u201d',aLine)
                        
                        replace = ''
                        
                        for anotherLine in s2:
                            replace += anotherLine
                        if replace != '':
                            info.append(replace)
                                
    if bool(oneWebsite):
        oneWebsite['description'] = info
        allWebSite.append(oneWebsite)
        
    json.dump(allWebSite,open("scrapeInfo2Json.json", "w"), indent = 6)
    
    return allWebSite
    
def scrapeInfoThreeToJson():
    
    f = open("scrapeInfo3.txt","r")
    
    website = {}
    
    title = ''
    count = 1
    numTags = 0
    numInfo = 0
    allInfo = []
    theInfo = {}
    totalInfo = []
    info = []
    tags = []
    
    for x in f:
        if title == '':
            if x == '\n':
                continue
            title = x[0:len(x) - 1]
            
            y = title.split('\u2013')
            title = ''
            
            for line in y:
                if line[0] != ' ':
                    title += line
                else:
                    title += r'-'+ line

            website['title'] = title
            
        elif x[0] == str(count): #create new table
            if len(tags) > 0:
                for y in allInfo:
                    theInfo = {}
                    theInfo[tags[0]] = y[0]
                    theInfo[tags[1]] = y[1]
                    theInfo[tags[2]] = y[2]
                    totalInfo.append(theInfo)
            count += 1
            numTags = 0
            tags = []
            allInfo = []
        elif numTags <= 2:
            
            y = x.split('\u2019')
            result = ''
            for line in y:
                result += line
            
            tags.append(result[0:len(result) - 1])
            numTags += 1
        elif numInfo < 3:
            numInfo += 1
            
            if numInfo == 1:
                if x == '\n' or x[0] == ' ':
                    y = allInfo[len(allInfo) - 1]
                    info.append(y[0])
                    continue
            
            info.append(x[0:len(x) - 1])
            if numInfo == 3:
                allInfo.append(info)
                numInfo = 0
                info = []
    
    for y in allInfo:
        theInfo = {}
        theInfo[tags[0]] = y[0]
        theInfo[tags[1]] = y[1]
        theInfo[tags[2]] = y[2]
        totalInfo.append(theInfo)
    
    website['information'] = totalInfo
    json.dump(website,open("scrapeInfo3Json.json","w"), indent = 6)
    
    return website
    
def scrapeInfoFourToJson():
    
    f = open("scrapeInfo4.txt","r")
    
    start = False
    sectionStart = False
    
    allWebsite = []     #Contains all websites
    oneWebsite = {}     #Contains a website's title + information
    oneWebsiteInfo = []
    
    title = ''          #Contains the website's title
    info = []           #Contains the website's information in order
    tableTags = []      #Contains the tags 
    
    oneRow = {}
    
    count = 0
    aCount = 0
    countRef = 0
    total = 0
    
    for x in f:
        
        if x == '\n':           # This portion skips the new line
            
            if len(tableTags) > 0:
                print(tableTags)
                tableTags = []
                
            if start == False:
                start = True
                sectionStart = False
            else:
                start = False
                sectionStart = True
            continue
        
        elif start == True:     #This stores information about a course if the title isn't empty
           
            if len(oneWebsiteInfo) >= 1:
                oneWebsite['info'] = oneWebsiteInfo
                allWebsite.append(oneWebsite)
                oneWebsiteInfo = []
           
            oneWebsite = {}     #Contains a website's title + information
            
            title = ''          #Contains the website's title
            info = []           #Contains the website's information in order
            
        elif sectionStart == True:
            if title == '':
                
                tableTags = []
                
                title = x[0:len(x) - 1]
                print(title)
                y = title.split('\u2013')
                replace = ''
                for line in y:
                    if line[0] == ' ':
                        replace += '-'+line
                    else:
                        replace += line
                
                oneWebsite['title'] = str(replace)
            elif len(x) <= 2: #Start of a new table
                
                y = int(x[0])
                if len(tableTags) > 0:
                    #print(tableTags)
                    print()
                
                tableTags = []
                
                if y == 9:
                    count = 9
                    total = 9
                    countRef = 9
                elif y == 6:
                    count = 6
                    total = 6
                    countRef = 6
                elif y == 4:
                    count = 4
                    total = 4
                    countRef = 4
                
            elif count > 0:
                count -= 1
                tableTags.append(x[0:len(x) - 1])
            else:
                if total > 0:
                    
                    total -= 1
                    info.append(x[0:len(x) - 1])
                    
                    if total == 0:
                        total = int(countRef)
                        #print(info)
                        
                        aCount = 0
                        
                        for x in tableTags: #Tie information with the TableTags
                            
                            oneRow[x] = info[aCount]
                            aCount += 1
                        
                        oneWebsiteInfo.append(oneRow)
                        
                        info = []
                        oneRow = {}
    
    if len(oneWebsiteInfo) >= 1:
        oneWebsite['info'] = oneWebsiteInfo
        allWebsite.append(oneWebsite)
    
    for x in allWebsite:
        print(x)
    
    json.dump(allWebsite,open("scrapeInfo4Json.json","w"), indent = 6)
    
    return allWebsite
    
def scrapeInfoFiveToJson():
    
    f = open("scrapeInfo5.txt","r")
    
    start = False
    sectionStart = False
    
    allWebSite = []     #Contains all websites
    oneWebsite = {}     #Contains a website's title + information
            
    title = ''          #Contains the website's title
    sectionTitle = ''
    info = []           #Contains the website's information in order
    tableTags = []      #Contains the tags 
    oneWebsiteInfo = []
    sectionInfo = {}
    oneSection = []
    count = 0
    countRef = 0
    total = 0
    
    for x in f:
        
        if x == '\n':           # This portion skips the new line
            
            if count == 2 or count == 5:
                count += 1
                continue
            
            count += 1
               
            if start == False:
                start = True
                sectionStart = False
            else:
                start = False
                sectionStart = True
            continue
        
        elif start == True:     #This stores information about a course if the title isn't empty
               
            title = ''          #Contains the website's title
            
        elif sectionStart == True:
            if title == '':
                title = x[0:len(x) - 1]
                
                #issue here! look/read into it
                
                if len(sectionTitle) >= 1:
                    info.append(oneWebsiteInfo) #not sure
                    sectionInfo['info'] = oneWebsiteInfo 
                    oneSection.append(sectionInfo) #a section is stored here. refresh when new title
                    oneWebsite['info'] = oneSection
                    allWebSite.append(oneWebsite)
                    oneWebsite = {}
                
                y = x.split('\u2013')
                
                aLine = ''
                
                for line in y:
                    if line[0] == ' ':
                        aLine += '-'+ line
                    else:
                        aLine += line
                        
                
                oneWebsite['title'] = aLine[0:len(aLine) - 1]
                info = []
                oneSection = []
                sectionInfo = {}
                oneWebsiteInfo = []
                
            elif len(x) <= 2:   #Start of a section so #
                
                if len(sectionTitle) >= 1:
                    info.append(oneWebsiteInfo) #not sure
                    sectionInfo['info'] = oneWebsiteInfo 
                    
                    if sectionInfo.get('title') is not None:
                        oneSection.append(sectionInfo) 
                
                    oneWebsiteInfo = []
                    sectionInfo = {}
                
                sectionTitle = ''
            elif sectionTitle == '': #title of a section
                
                sectionTitle = x[0:len(x) - 1]
                
                y = re.split('"|(.)',sectionTitle)
    
                aLine = ''
                for line in y:
                    if line != '' and line is not None:
                        aLine += line
                
                sectionInfo['title'] = aLine
            else:
                
                y = x.split('\n')
                
                for line in y:
                    if line != '':
                        oneWebsiteInfo.append(line)
        
    
    if len(info) >= 1:
        sectionInfo['info'] = oneWebsiteInfo
        oneSection.append(sectionInfo) #a section is stored here. refresh when new title
        oneWebsite['info'] = oneSection
        allWebSite.append(oneWebsite)
    
    json.dump(allWebSite,open("scrapeInfo5Json.json","w"), indent = 6)
    
    return allWebSite
    
def scrapeInfoSixToJson():
    
    f = open("scrapeInfo6.txt","r")
    
    start = False
    sectionStart = False
    sectionInfo = False
    
    allWebSite = []     #Contains all websites
    oneWebsite = {}     #Contains a website's title + information
            
    title = ''          #Contains the website's title
    sectionTitle = ' '
    
    tableTags = []      #Contains the tags 
    count = 0
    
    info = []    
    
    allLists = []
    
    aList = {}
    listPoints = []
    
    countRef = 0
    total = 0
    
    for x in f:
        
        if x == '\n':           # This portion skips the new line
            if len(tableTags) > 0:
                print(tableTags)
                tableTags = []
                
            if start == False:
                start = True
                sectionStart = False
            else:
                start = False
                sectionStart = True
            continue
        
        elif start == True:     #This stores information about a course if the title isn't empty
            
            title = ''          #Contains the website's title
            
        elif sectionStart == True:
            if title == '':
                title = x[0: len(x) - 1]
                
                if oneWebsite.get('title') is not None:
                    if sectionTitle != '':
                        aList['info'] = listPoints
                        
                        if len(listPoints) >= 1:
                            allLists.append(aList)
                        listPoints = []
                        aList = {}
                    
                    oneWebsite['info'] = info
                    
                    if len(allLists) >= 1:
                        oneWebsite['list'] = allLists
                    allWebSite.append(oneWebsite)
                 
                oneWebsite = {}     #Contains a website's title + information
                info = []
                allLists = []
                oneWebsite['title'] = title
            elif len(x) <= 2:
                
                count += 1
                if count % 2 == 1:
                    
                    if sectionTitle != '':
                        aList['info'] = listPoints
                        if len(listPoints) >= 1:
                            allLists.append(aList)
                        listPoints = []
                        aList = {}
                    
                    sectionTitle = ''
                
                if sectionInfo == False:
                    sectionInfo = True
                else:
                    sectionInfo = False
                
            elif sectionTitle == '': #title of list
                sectionTitle = x[0:len(x) - 1]
                aList['title'] = sectionTitle
            elif sectionInfo == True: #info in list
                listPoints.append(x)
            else:
                y = x.split('\n')
                
                for line in y:
                    if line != '':
                        info.append(line)
                        
    if oneWebsite.get('title') is not None:
        if sectionTitle != '':
            aList['info'] = listPoints
            if len(listPoints) >= 1:
                allLists.append(aList) 
        oneWebsite['info'] = info
        oneWebsite['list'] = allLists
        allWebSite.append(oneWebsite)
    for x in allWebSite:
        print(x)
    
    json.dump(allWebSite,open("scrapeInfo6Json.json","w"), indent = 6)
    
    return allWebSite
    
def scrapeDirect():
    f = open("resultText.txt","r")
    
    allLinks = []
    link = {}
    
    aTitle = ""
    aLink = ""
    
    for x in f:
        
        if len(x) == 2 or len(x) == 3:
            if aTitle != "":
                link['title'] = aTitle
                link['website'] = aLink
                allLinks.append(link)
            aTitle = ""
            aLink = ""
            link = {}
        elif len(x) == 1:
            continue
        else:
            if aTitle == "":
                y = x[0:len(x) - 1]
                
                line = y.split('\u00a8C ')
                
                y = ''
                
                for aLine in line:
                    y += aLine 
                
                aTitle = y
            else:
                aLink = x[0:len(x) - 1]
    
    link['title'] = aTitle
    link['website'] = aLink
    allLinks.append(link)
    
    json.dump(allLinks,open("resultText.json","w"), indent = 6)
    
    return allLinks
    
def main():
    
    list3 = []
    
    list1 = scrapeInfoOneToJson()
    list2 = scrapeInfoTwoToJson()
    list3.append(scrapeInfoThreeToJson())
    list4 = scrapeInfoFourToJson()
    list5 = scrapeInfoFiveToJson()
    list6 = scrapeInfoSixToJson()
    list7 = scrapeDirect()
    
    finalList = list1+list2+list3+list4+list5+list6+list7
    
    json.dump(finalList,open("finalList.json","w"), indent = 6)
    
main()