from selenium import selenium
import unittest, time, re
import SolusModels

def wait_then_click(sel, identifier):
    while not sel.is_element_present(identifier):
        print "Login button not present. Waiting 3 seconds..."
        time.sleep(3)
    sel.click(identifier)

class selenium_export(unittest.TestCase):
    
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://sso.queensu.ca/amserver/UI/Login")
        self.selenium.start()
        
        
        #Data to be kept
        self.courses = []
        self.unique_attributes = {}
        
        #Temporary data
        self.current_term = ""
        
        #Test parameters
        
        #Which letters of courses to go through
        #alphanums = string.ascii_uppercase + string.digits #"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.alphanums = "C"
        
        #Optional cap for number of subjects per letter to scrape
        #Set to 0 to have no cap
        self.max_subjects_per_letter = 1
        
        #Which index of subject dropdowns to start at in a given alphanum
        self.starting_subject_index = 4
        
        #Optional cap for number of courses per subject to scrape
        #Set to 0 to have no cap
        self.max_courses_per_subject = 7
        
        #Which index of coursesto start at in a given subject
        self.starting_course_index = 0
        
    
    def test_selenium_export(self):
        sel = self.selenium
        sel.open("/amserver/UI/Login")
        
        #Get login information from config file
        with open('../ignored_files/selenium_config.txt', 'r') as config_file:
            line_num = 0
            login_info = ['','']
            for line in config_file:
                login_info[line_num] = line.strip()
                line_num += 1
          
        #Enter Credentials
        sel.type("id=IDToken1", login_info[0])
        sel.type("id=IDToken2", login_info[1])
        
        #Log in
        sel.click("name=Login.Submit")
        sel.wait_for_page_to_load("30000")
        
        #Get URL for SOLUS and open it
        solus_url = sel.get_attribute("link=SOLUS Student Centre@href")
        sel.open(solus_url)
        
        #Get to content frame
        sel.select_frame("name=TargetContent")
        
        #"Search For Classes"
        sel.click("id=DERIVED_SSS_SCL_SSS_GO_4$229$")
        sel.wait_for_page_to_load("30000")
        
        #"browse course catalog"
        sel.click("link=browse course catalog")
        sel.wait_for_page_to_load("30000")
        
        
        print "Navigation to SOLUS complete. Beginning scraping..."
        
        
        #Go through all the course catalogue pages
        
        for alphanum in self.alphanums:
            self.scrape_subjects_for_alphanum(alphanum)
        
        print "Scraped a total of %d courses" % SolusModels.SolusCourse.num_courses
        print "Unique Attributes were:"
        
        for key in self.unique_attributes:
            print "(%s): %s" % (self.unique_attributes[key], key)
        
        #for course in self.courses:
            #course.describe()
        
        import pdb; pdb.set_trace()
    
    #
    # Alphanum
    #
    
    def scrape_subjects_for_alphanum(self, alphanum):
        sel = self.selenium
        sel.click("id=DERIVED_SSS_BCC_SSR_ALPHANUM_" + alphanum)
        sel.wait_for_page_to_load("30000")
        
        
        #Prepare to traverse all links
        link_number = self.starting_subject_index
        link_name_base = "name=DERIVED_SSS_BCC_SSR_EXPAND_COLLAPS$IMG$%d"
        link_name = link_name_base % (link_number,)
        
        while sel.is_element_present(link_name):
            #Open the dropdown
            sel.click(link_name)
            sel.wait_for_page_to_load("30000")
            
            #Traverses all course links in the dropdown
            self.scrape_single_dropdown()
            
            #Close the dropdown
            try:
                sel.click(link_name)
            except:
                print "FAILURE %s" % link_name
                time.sleep(100)
                
            sel.wait_for_page_to_load("30000")
            
            #Go to next link
            link_number += 1
            if self.max_subjects_per_letter and link_number >= self.max_subjects_per_letter + self.starting_subject_index:
                break
            
            link_name = link_name_base % (link_number,)
            
    #
    # Subject
    #    
    
    def scrape_single_dropdown(self):
        sel = self.selenium
        
        #Prepare to traverse all links
        link_number = self.starting_course_index
        link_name_base = "id=CRSE_TITLE$%d"
        link_name = link_name_base % (link_number,)
        
        while sel.is_element_present(link_name):
            #Go into the course
            sel.click(link_name)
            sel.wait_for_page_to_load("30000")
            
            self.course = SolusModels.SolusCourse()
            self.courses.append(self.course)
        
            SolusModels.SolusCourse.num_courses += 1
            
            #Scrape info from course
            try:
                self.scrape_single_course()
            except SolusModels.UselessCourseException as e:
                print "Ignored"
                self.courses.pop()
                SolusModels.SolusCourse.num_courses -= 1
            
            #Back out from course page
            sel.click("id=DERIVED_SAA_CRS_RETURN_PB")
            sel.wait_for_page_to_load("30000")
            
            #Go to next course
            link_number += 1
            
            if self.max_courses_per_subject and link_number >= self.max_courses_per_subject + self.starting_course_index:
                break
            
            link_name = link_name_base % (link_number,)
    
    #
    # Course
    #
    
    def scrape_single_course(self):
        sel = self.selenium
        
        self.scrape_title()
        self.scrape_attributes()
        self.scrape_description()
        self.show_and_scrape_sections()
        
    #
    # Course - Title
    #
    
    def scrape_title(self):
        sel = self.selenium
        raw_title = sel.get_text("css=span.PALEVEL0SECONDARY").strip()
        
        m = re.search('^([\S]+)\s+([\S]+)\s+-\s+(.*)$', raw_title)
        
        self.course.subject = m.group(1)
        self.course.num = m.group(2)
        self.course.title = m.group(3)

        print ""
        print "%s %s - %s" % (self.course.subject, self.course.num, self.course.title)
        
        if re.search('^(UNSP)|(.*UNS)$', self.course.num):
            raise SolusModels.UselessCourseException("%s %s" % (self.course.subject, self.course.num))

            
    #
    # Course - Attributes
    #
    
    def scrape_attributes(self):
        sel = self.selenium

        titles = []
        title_locator_formats = ["xpath=(//label[@class='PSDROPDOWNLABEL'])[%d]", "xpath=(//label[@class='PSEDITBOXLABEL'])[%d]"]
        
        values = []
        value_locator_formats = ["xpath=(//span[@class='PSDROPDOWNLIST_DISPONLY'])[%d]","xpath=(//span[@class='PSEDITBOX_DISPONLY'])[%d]"]
        
        for format in title_locator_formats:
            self.add_entries_for_position(titles, format)
        
        
        for format in value_locator_formats:
            self.add_entries_for_position(values, format)
        
        
        info_mappings = {}
        
        for (title_text, title_pos) in titles:
            if title_text not in self.unique_attributes:
                self.unique_attributes[title_text] = "%s %s" % (self.course.subject, self.course.num)

        
        for (value_text, value_pos) in values:
            
            best_diff = 10000
            best_text = None
            for (title_text, title_pos) in titles:
                diff = abs(title_pos - value_pos)
                if value_pos > title_pos - 5 and diff < best_diff:
                    best_diff = diff
                    best_text = title_text
                
            if best_text:
                if best_text in info_mappings:
                    info_mappings[best_text] += " " + value_text
                else:
                    info_mappings[best_text] = value_text
            else:
                print "No match for %s" % value_text
                
    def add_entries_for_position(self, lis, locator_format_string):
        sel = self.selenium
        index = 1
        locator = locator_format_string % index
        while sel.is_element_present(locator):
            lis.append((sel.get_text(locator).strip(), sel.get_element_position_top(locator)))
                    
            index += 1
            locator = locator_format_string % index
    
    #
    # Course - Description
    #
    
    
    def scrape_description(self):
        sel = self.selenium
        description_locator = "xpath=(//span[@class='PSLONGEDITBOX'])[1]"
        if sel.is_element_present(description_locator):
            self.course.description = sel.get_text(description_locator)
            #print "Description: %s" % course.description
    
            
    #
    # Course - Sections
    #
    
    
    def show_and_scrape_sections(self):
        sel = self.selenium
        
        #Check for "view class sections"
        if sel.is_element_present("id=DERIVED_SAA_CRS_SSR_PB_GO"):
            
            sel.click("id=DERIVED_SAA_CRS_SSR_PB_GO")
            sel.wait_for_page_to_load("30000")
            
            self.course.is_scheduled = True
            
            self.scrape_sections()
        else:
            self.course.is_scheduled = False
    
    def scrape_sections(self):
        sel = self.selenium
        
        term_options = sel.get_select_options("id=DERIVED_SAA_CRS_TERM_ALT")
        
        for option in term_options:
            if not len(term_options) == 1:
                sel.select("id=DERIVED_SAA_CRS_TERM_ALT", "label=%s" % option)
                sel.click("id=DERIVED_SAA_CRS_SSR_PB_GO$92$")
                sel.wait_for_page_to_load("30000")
            
            self.current_term = option
            self.scrape_term()
        
    #
    # Term
    #
    
    def scrape_term(self):
        sel = self.selenium
        
        if sel.is_element_present("id=CLASS_TBL_VW5$fviewall$0"):
            sel.click("id=CLASS_TBL_VW5$fviewall$0")
            sel.wait_for_page_to_load("30000")

        self.scrape_section_page()
        
    #
    # Section Page
    #
    
    def scrape_section_page(self):
        
        section_pieces = self.section_pieces_from_page()
        
        while len(section_pieces) > 0:
            section = SolusModels.Section()
            self.course.sections.append(section)
            
            section.term = self.current_term
            
            self.scrape_single_section(section_pieces, section)
            
            
        
    def section_pieces_from_page(self):
        sel = self.selenium
        
        
        
        section_pieces = []
        index = 1
        locator_format = "xpath=(//td[@class='PSLEVEL2GRIDROW'])[%d]"
        locator = locator_format % index
                
        while sel.is_element_present(locator):
            
            section_pieces.append(sel.get_text(locator).strip())
            
            index += 1
            locator = locator_format % index
        
        return section_pieces
    
    def scrape_single_section(self, piece_array, section):
        while not self.next_row_is_section_header(piece_array):
            timeslot = SolusModels.Timeslot()
            section.timeslots.append(timeslot)
            
            self.scrape_single_timeslot(piece_array, timeslot)
        
        self.scrape_section_header(piece_array, section)
    
    
    def next_row_is_section_header(self, piece_array):
        if piece_array[-1] == "Select":
            return True
        
        for i in range (-1, -6, -1):
            if re.search('^([\S]+)-([\S]+)\s+\((\S+)\)$', piece_array[i]):
                return True
        
        return False
    
    def scrape_single_timeslot(self, piece_array, timeslot):
        if len(piece_array) < 6:
            import pdb; pdb.set_trace()
        
        timeslot.date_range = piece_array.pop()
        timeslot.instructor = piece_array.pop()
        timeslot.room = piece_array.pop()
        timeslot.end = piece_array.pop()
        timeslot.start = piece_array.pop()
        timeslot.day = piece_array.pop()
    
    def scrape_section_header(self, piece_array, section):
        section_info = piece_array.pop()
        m = re.search('^([\S]+)-([\S]+)\s+\((\S+)\)$', section_info)
        
        while not m:
            section_info = piece_array.pop()
            m = re.search('^([\S]+)-([\S]+)\s+\((\S+)\)$', section_info)
        
        section.index = m.group(1)
        section.type = m.group(2)
        section.id = m.group(3) 
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


