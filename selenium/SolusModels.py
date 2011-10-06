class SolusCourse:
    
    num_courses = 0
    
    def __init__(self):
        self.title = ""
        self.subject = ""
        self.num = ""
        
        self.description = ""
        
        self.is_scheduled = True
        
        self.sections = []

        
    def add_merged_info(self, first, second):
        self.title = first.title
        self.subject = first.subject
        self.num = first.num[:-1]
        
        self.description = first.description
        
        self.is_scheduled = first.is_scheduled
        
        self.sections = []
        
        for s1 in first.sections:
            for s2 in second.sections:
                if s1.index == s2.index:
                    s1.id += ",%s" % s2.id
                    s1.term += ",%s" % s2.term
                    s1.timeslots += s2.timeslots
                    self.sections.append(s1)
                    break
    
    def get_key(self):
        return "%s %s" % (self.subject, self.num)
    
    def clean(self):
        for section in self.sections:
            section.clean()
    
    def describe(self):
        print u"\n\nCourse:\n(%s %s) %s" % (self.subject, self.num, self.title)
        if self.is_scheduled:
            print "This course is scheduled."
        else:
            print "This course is not scheduled."
        print self.description
        for section in self.sections:
            section.describe()


class Section:
    def __init__(self):
        self.index = ""
        self.type = ""
        self.id = ""
        self.term = ""
        self.timeslots = []
    
    def clean(self):
        for timeslot in self.timeslots:
            print timeslot.clean()
    
    def describe(self):
        print u"\nSection:\n(%s) %s-%s, %s" % (self.id, self.type, self.index, self.term)
        for timeslot in self.timeslots:
            timeslot.describe()

class Timeslot:
    def __init__(self):
        self.day = ""
        self.start = ""
        self.end = ""
        self.room = ""
        self.instructor = ""
        self.date_range = ""
    
    def clean(self):
        self.instructor = self.instructor.replace(" \n ", " ")
    
    def describe(self):
        print u"%s, %s-%s in %s, with %s. %s" % (self.day, self.start, self.end, self.room, self.instructor, self.date_range)
    

class UselessCourseException(Exception):
    def __init__(self, course_code):
        self.course_code = course_code
    def __str__(self):
        return repr(self.course_code)