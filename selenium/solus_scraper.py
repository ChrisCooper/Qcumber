from selenium import selenium
import unittest, time, re
from SolusModels import SolusCourse

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
        
        self.courses = []
    
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
        alphanums = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for alphanum in alphanums:
            self.scrape_courses_for_alphanum(alphanum)
        
    def scrape_courses_for_alphanum(self, alphanum):
        sel = self.selenium
        sel.click("id=DERIVED_SSS_BCC_SSR_ALPHANUM_" + alphanum)
        sel.wait_for_page_to_load("30000")
        
        
        #Prepare to traverse all links
        link_number = 0
        link_name_base = "name=DERIVED_SSS_BCC_SSR_EXPAND_COLLAPS$IMG$%d"
        link_name = link_name_base % (link_number,)
        
        while sel.is_element_present(link_name):
            #Open the dropdown
            sel.click(link_name)
            sel.wait_for_page_to_load("30000")
            
            #Traverses all course links in the dropdown
            self.scrape_single_dropdown()
            
            #Close the dropdown
            sel.click(link_name)
            sel.wait_for_page_to_load("30000")
            
            #Go to next link
            link_number += 1
            link_name = link_name_base % (link_number,)
        
    
    def scrape_single_dropdown(self):
        sel = self.selenium
        
        #Prepare to traverse all links
        link_number = 0
        link_name_base = "id=CRSE_TITLE$%d"
        link_name = link_name_base % (link_number,)
        
        while sel.is_element_present(link_name):
            #Go into the course
            sel.click(link_name)
            sel.wait_for_page_to_load("30000")
            
            #Scrape info from course
            self.scrape_single_course()
            
            #Back out from course page
            sel.click("id=DERIVED_SAA_CRS_RETURN_PB")
            sel.wait_for_page_to_load("30000")
            
            #Go to next course
            link_number += 1
            link_name = link_name_base % (link_number,)
    
    def scrape_single_course(self):
        sel = self.selenium
        
        course = SolusCourse()
        
        raw_title = sel.get_text("css=span.PALEVEL0SECONDARY").strip()
        
        m = re.search('^([\S]+)\s+([\S]+)\s+-\s+(.*)$', raw_title)
        
        course.subject = m.group(1)
        course.num = m.group(2)
        course.title = m.group(3)

        print "%s %s - %s" % (course.subject, course.num, course.title)
    
    def uncopied(self):
        sel.click("id=CRSE_TITLE$0")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SAA_CRS_RETURN_PB")
        sel.wait_for_page_to_load("30000")
        sel.click("id=CRSE_TITLE$8")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SAA_CRS_SSR_PB_GO")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SAA_CRS_RETURN_PB")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SSS_BCC_SSR_ALPHANUM_B")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SSS_BCC_GROUP_BOX_1$84$$1")
        sel.wait_for_page_to_load("30000")
        sel.click("id=CRSE_TITLE$8")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SAA_CRS_SSR_PB_GO")
        sel.wait_for_page_to_load("30000")
        sel.click("name=CLASS_TBL_VW5$fdown$img$0")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SAA_CRS_RETURN_PB")
        sel.wait_for_page_to_load("30000")
        sel.click("name=DERIVED_SSS_BCC_SSR_EXPAND_COLLAPS$IMG$1")
        sel.wait_for_page_to_load("30000")
        sel.click("name=DERIVED_SSS_BCC_SSR_EXPAND_COLLAPS$IMG$2")
        sel.wait_for_page_to_load("30000")
        sel.click("id=CRSE_TITLE$0")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
