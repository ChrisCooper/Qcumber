class SolusCourse:
    
    num_courses = 0
    
    def __init__(self):
        self.title = ""
        self.subject = ""
        self.num = ""
        
        self.description = ""
        
        self.sections = []
        self.num_courses += 1


class Section:
    def __init__(self):
        self.index = ""
        self.type = ""
        self.id = ""
        self.timeslots = []
        
    def __unicode__(self):
        desc = u"(%s) %s-%s\n" % (self.id, self.type, self.index)
        #for timeslot in self.timeslots:
         #   desc = desc + timeslot + u"\n"
        return desc

class Timeslot:
    def __init__(self):
        self.day = ""
        self.start = ""
        self.end = ""
        self.room = ""
        self.instructor = ""
        self.date_range = ""
    
    def __unicode__(self):
        return u"%s, %s-%s in %s, with %s. %s" % (self.day, self.start, self.end, self.room, self.instructor, self.date_range)