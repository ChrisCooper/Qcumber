class SolusCourse:
    
    num_courses = 0
    
    def __init__(self):
        self.title = ""
        self.subject = ""
        self.num = ""
        
        self.description = ""
        
        self.sections = []
    
    def clean(self):
        for section in self.sections:
            section.clean()
    
    def describe(self):
        print u"\n\nCourse:\n(%s %s) %s" % (self.subject, self.num, self.title)
        print self.description
        for section in self.sections:
            print section.describe()


class Section:
    def __init__(self):
        self.index = ""
        self.type = ""
        self.id = ""
        self.timeslots = []
    
    def clean(self):
        for timeslot in self.timeslots:
            print timeslot.clean()
    
    def describe(self):
        print u"\nSection:\n(%s) %s-%s" % (self.id, self.type, self.index)
        for timeslot in self.timeslots:
            print timeslot.describe()

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
    
