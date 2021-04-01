import json

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
                    
            elif courseStart == False and end == True:
                
                y = x.split('\n')
                
                if singleCourse.get('course name') is None:
                    
                    for line in y:
                        if line != '':
                            singleCourse['course name'] = line
                else:
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
                
                print(x)
                
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
    
def main():
    scrapeInfoOneToJson()
    
main()