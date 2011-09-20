from selenium import selenium
import unittest, time, re

def wait_then_click(sel, identifier):
    if not sel.check(identifier):
        sleep(3)
    sel.click(identifier)

class selenium_export(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://sso.queensu.ca/amserver/UI/Login")
        self.selenium.start()
    
    def test_selenium_export(self):
        sel = self.selenium
        sel.open("/amserver/UI/Login")
        
        with open('../ignored_files/selenium_config.txt', 'r') as config_file:
            line_num = 0
            login_info = ['','']
            for line in config_file:
                login_info[line_num] = line.strip()
                
                
        sel.type("id=IDToken1", login_info[0])
        sel.type("id=IDToken2", login_info[1])
        sel.click("name=Login.Submit")
        sel.wait_for_page_to_load("30000")
        
        wait_then_click(sel, "link=SOLUS Student Centre")
        
        #Ignore the alert
        sel.get_alert()
        
        sel.wait_for_popup("30000")
        
        #get the popup
        sel.select_window()
        
        sel.select_frame("TargetContent")
        sel.click("id=DERIVED_SSS_SCL_SSS_GO_4$229$")
        sel.wait_for_page_to_load("30000")
        sel.click("link=browse course catalog")
        sel.wait_for_page_to_load("30000")
        sel.click("id=DERIVED_SSS_BCC_SSR_ALPHANUM_A")
        sel.wait_for_page_to_load("30000")
        sel.click("name=DERIVED_SSS_BCC_SSR_EXPAND_COLLAPS$IMG$0")
        sel.wait_for_page_to_load("30000")
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
