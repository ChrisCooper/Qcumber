from selenium import selenium
import unittest, time, re
from SolusModels import SolusCourse

verificationErrors = []
sel = selenium("localhost", 4444, "*chrome", "https://sso.queensu.ca/amserver/UI/Login")
sel.start()

sel.open("/amserver/UI/Login")
        
#Get login information from config file
with open('../ignored_files/selenium_config.txt', 'r') as config_file:
    line_num = 0
    login_info = ['','']
    for line in config_file:
        login_info[line_num] = line.strip()
        line_num += 1


sel.type("id=IDToken1", login_info[0])
sel.type("id=IDToken2", login_info[1])
        
sel.click("name=Login.Submit")
sel.wait_for_page_to_load("30000")
               
solus_url = sel.get_attribute("link=SOLUS Student Centre@href")

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



sel.click("id=DERIVED_SSS_BCC_SSR_ALPHANUM_C")
sel.wait_for_page_to_load("30000")
        
#Prepare to traverse all links
link_number = 0
link_name_base = "name=DERIVED_SSS_BCC_SSR_EXPAND_COLLAPS$IMG$6"
link_name = link_name_base
        
sel.click(link_name)
sel.wait_for_page_to_load("30000")
            
        
    
        
#Prepare to traverse all links
link_number = 0
link_name_base = "id=CRSE_TITLE$10"
link_name = link_name_base
        
#Go into the course
sel.click(link_name)
sel.wait_for_page_to_load("30000")
            
        
course = SolusCourse()
        
raw_title = sel.get_text("css=span.PALEVEL0SECONDARY").strip()
        
m = re.search('^([\S]+)\s+([\S]+)\s+-\s+(.*)$', raw_title)
        
course.subject = m.group(1)
course.num = m.group(2)
course.title = m.group(3)

print "%s %s - %s" % (course.subject, course.num, course.title)



   #
   #
   # USE (X,Y) COORDINATES OF THE FOLLOWING TO FIGURE OUT WHICH VALUE CORRESPONDS TO WHICH TITLE
   #
   #

#titles
sel.get_text("xpath=(//label[@class='PSDROPDOWNLABEL'])[1]")
sel.get_text("xpath=(//label[@class='PSEDITBOXLABEL'])[1]")

#values
sel.get_text("xpath=(//span[@class='PSDROPDOWNLIST_DISPONLY'])[1]")
sel.get_text("xpath=(//span[@class='PSEDITBOX_DISPONLY'])[1]")

#description
sel.get_text("xpath=(//span[@class='PSLONGEDITBOX'])[1]")

#Seems to get full page text
#sel.get_text("id=ACE_width")

#Career Undergraduate Units 3.00 Grading Basis Graded Laboratory Required Lecture Required Course Components
raw_course_detail_box = sel.get_text("class=PSGROUPBOX").strip()

m = re.search('^Career(.*)Units(.*)Grading Basis\s+(\S*)\s*(.*)\s+Course Components$', raw_course_detail_box)

course.career = m.group(1).strip()
course.units = m.group(2).strip()
course.grading_basis = m.group(3).strip()
course.course_components = m.group(4).strip()

raw_enrollment_information_box = sel.get_text("class=PSGROUPBOXNBO").strip()


#Check for "view class sections"
if sel.is_element_present("id=DERIVED_SAA_CRS_SSR_PB_GO"):
        sel.click("id=DERIVED_SAA_CRS_SSR_PB_GO")
