import json
import re
import collections

#Name: Kenny Yang - 5934104
#The following python script will only be using json to translate a text document into a json file

class course:
    def __init__ (self, title):
        self.courseTitle = title
        self.courseDescription = []
        self.courses = []
        
    def addDescription(self, desc):    
        self.courseDescription.append(desc)
        
    def addCourse(self, aCourse):
        self.courses.append(aCourse)
        
class adminInfo:
    def __init__(self, position):
        self.position = position
        self.name = ''
        self.contact = ''
        self.office = ''
        self.eContact = ''
        
    def addName(self, name):
        self.name = name
    
    def addContact(self, number):
        self.contact = number

    def addOffice(self,office):
        self.office = office
    
    def addEmail(self, email):
        self.eContact = email
    
class courseInfo:
    def __init__(self, courseID):
        self.courseID = courseID
        self.courseName = ''
        self.courseInfo = []
    
    def getCourseName(self):
        return self.courseName
    
    def addCourseName(self, name):
        self.courseName = name
    
    def addCourseInfo(self, info):
        self.courseInfo.append(info)

def scrapeInfoToJson():
    
    f = open("testjson.txt","r")
    f1 = open("testJson.json","w")
    
    start = False
    end = False
    sectionStart = False
    courseStart = False
    tAdmin = False
    count = 0
    
    title = ''
    
    aCourse = courseInfo(' ')
    
    for x in f:
        
        if x == '\n':
            if start == False:
                start = True
                sectionStart = False
            else:
                start = False
                sectionStart = True
            continue
        if start == True:
            oneCourse = {}
            oneCourse_desc = []
            singleCourses = []
            singleCourse = {}
            singleCourseInfo = []
            print(x)
        
        if sectionStart == True:
            if title == '':
                title = x
                theCourse = course(title)
                y = x.split('\n')
                for line in y:
                    if line != '':
                        oneCourse['title'] = line
            elif len(x) <= 12 and len(x) > 6 and tAdmin == False:
                if x[5] == ' ' or x[4] == ' ':
                    if bool(singleCourse):
                            print("NEW COURSE")
                            singleCourse['course description'] = oneCourse_desc
                            singleCourses.append(singleCourse)
                    if aCourse.getCourseName() != '':
                        singleCourse = {}
                        singleCourseInfo = []
                        theCourse.addCourse(aCourse)
                    courseStart = True
                    aCourse = courseInfo(x)
                    
                    y = x.split('\n')
                    for line in y:
                        s = line.split('#')
                        for aLine in s:
                            if aLine != '':
                                singleCourse['course ID'] = aLine
                    print(x)
            elif courseStart == False:
                y = x.split('. ')
                for line in y:
                    s = line.split('\n')
                    theCourse.addDescription(line)
                    for aLine in s:
                        if aLine != '':
                            oneCourse_desc.append(aLine)
                    #print(line)
            elif aCourse.getCourseName() == '':
                aCourse.addCourseName(x)
                
                y = x.split('\n')
                
                for line in y:
                    if line != '':
                        singleCourse['course name'] = line
                #print(x)
            elif str(x.strip('\n')) == "Administrative Assistant":
                #print("TRUEEEE")
                tAdmin = True
                anAdmin = adminInfo(x)
            elif tAdmin == True:
                count += 1
                if count == 5:
                    tAdmin = False
                    end = True
                    continue
                if count == 1:
                    anAdmin.addName(x)
                elif count == 2:
                    anAdmin.addContact(x)
                elif count == 3:
                    anAdmin.addOffice(x)
                else:
                    anAdmin.addEmail(x)
            elif end == True:
                y = y = x.split('. ')
                for line in y:
                    s = line.split('\n')
                    theCourse.addDescription(line)
                    for aLine in s:
                        if aLine != '':
                            oneCourse_desc.append(aLine)
            else:
                aCourse.addCourseInfo(x)
                singleCourseInfo.append(x)
                #print(x)
     
    oneCourse['description'] = oneCourse_desc
    singleCourse['course description'] = oneCourse_desc
    singleCourses.append(singleCourse)
    oneCourse['available courses'] = singleCourses
    json.dump(oneCourse, f1, indent = 6)            
    for line in singleCourses:
        print(line)
    #llCourse = json.dumps(theCourse.__dict__)
    #print(allCourse)
    #json.dump(json.dumps(theCourse.__dict__), f1, indent = 6)
scrapeInfoToJson()