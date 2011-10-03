from selenium import selenium
import unittest, time, re
import SolusModels

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



sel.click("id=DERIVED_SSS_BCC_SSR_ALPHANUM_B")
sel.wait_for_page_to_load("30000")
        
#Prepare to traverse all links
link_number = 0
link_name_base = "name=DERIVED_SSS_BCC_SSR_EXPAND_COLLAPS$IMG$1"
link_name = link_name_base
        
sel.click(link_name)
sel.wait_for_page_to_load("30000")
            
        
    
        
#Prepare to traverse all links
link_number = 0
link_name_base = "id=CRSE_TITLE$8"
link_name = link_name_base
        
#Go into the course
sel.click(link_name)
sel.wait_for_page_to_load("30000")
            
        
course = SolusModels.SolusCourse()
        
raw_title = sel.get_text("css=span.PALEVEL0SECONDARY").strip()
        
m = re.search('^([\S]+)\s+([\S]+)\s+-\s+(.*)$', raw_title)
        
course.subject = m.group(1)
course.num = m.group(2)
course.title = m.group(3)

print "%s %s - %s" % (course.subject, course.num, course.title)





titles = []
title_locator_formats = ["xpath=(//label[@class='PSDROPDOWNLABEL'])[%d]", "xpath=(//label[@class='PSEDITBOXLABEL'])[%d]"]

values = []
value_locator_formats = ["xpath=(//span[@class='PSDROPDOWNLIST_DISPONLY'])[%d]","xpath=(//span[@class='PSEDITBOX_DISPONLY'])[%d]"]


def add_entries_for_position(sel, lis, locator_format_string):
    index = 1
    locator = locator_format_string % index
    while sel.is_element_present(locator):
        lis.append((sel.get_text(locator).strip(), sel.get_element_position_top(locator)))
            
        index += 1
        locator = locator_format_string % index




for format in title_locator_formats:
    add_entries_for_position(sel, titles, format)


for format in value_locator_formats:
    add_entries_for_position(sel, values, format)


info_mappings = {}

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

for key in info_mappings:
    print "%s: %s" % (key, info_mappings[key])

description_locator = "xpath=(//span[@class='PSLONGEDITBOX'])[1]"
if sel.is_element_present(description_locator):
    course.description = sel.get_text(description_locator)
    #print "Description: %s" % course.description

sel.click("id=DERIVED_SAA_CRS_SSR_PB_GO")
sel.wait_for_page_to_load("30000")





section_pieces = []

index = 1

locator_format = "xpath=(//td[@class='PSLEVEL2GRIDROW'])[%d]"
locator = locator_format % index
        
while sel.is_element_present(locator):
    
    section_pieces.append(sel.get_text(locator).strip())
    
    index += 1
    locator = locator_format % index



def scrape_single_section(piece_array, section):
    while not next_row_is_section_header(piece_array):
        timeslot = SolusModels.Timeslot()
        scrape_single_timeslot(piece_array, timeslot)
        section.timeslots.append(timeslot)
    
    scrape_section_header(piece_array, section)

def next_row_is_section_header(piece_array):
    return piece_array[-1] == "Select"

def scrape_section_header(piece_array, section):
    piece_array.pop()
    piece_array.pop()
    piece_array.pop()
    
    section_info = piece_array.pop()
    
    m = re.search('^([\S]+)-([\S]+)\s+\((\S+)\)$', section_info)
    if m:
        section.index = m.group(1)
        section.type = m.group(2)
        section.id = m.group(3)

def scrape_single_timeslot(piece_array, timeslot):
    
    timeslot.date_range = piece_array.pop()
    timeslot.instructor = piece_array.pop()
    timeslot.room = piece_array.pop()
    timeslot.end = piece_array.pop()
    timeslot.start = piece_array.pop()
    timeslot.day = piece_array.pop()


    
while len(section_pieces) > 0:
    section = SolusModels.Section()
    scrape_single_section(section_pieces, section)
    
    course.sections.append(section)


course.clean()
course.describe()


