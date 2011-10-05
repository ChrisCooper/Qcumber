class SolusCourse:
    
    num_courses = 0
    
    def __init__(self):
        self.title = ""
        self.subject = ""
        self.num = ""
        
        self.description = ""
        
        self.sections = []
        
        self.is_scheduled = True
    
    def clean(self):
        for section in self.sections:
            section.clean()
    
    def describe(self):
        print u"\n\nCourse:\n(%s %s) %s" % (self.subject, self.num, self.title)
        if self.is_scheduled:
            print "This course is scheduled"
        else:
            print "This course is not scheduled"
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