
class HomePage():
    
    def __init__(self,driver):
        self.driver = driver
        self.driver.linkTest_by_linkT = "Run Your Fleet"
        
        
    def equalTest(self, driver):
        self.driver.find_element_by_link_text(self.driver.linkTest_by_linkT)
        
        
        
       # self.driver.find_element_by_partial_link_text(self.driver.linkTest_by_partial).click()