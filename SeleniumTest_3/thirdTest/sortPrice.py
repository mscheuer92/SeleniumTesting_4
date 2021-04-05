#2nd Page, clicking on "lower than $13.00"

class SortPrice():
    
    def __init__(self, driver):
        self.driver = driver
        self.sort_by_link_text = "Under $13.00"
        
    
        
    def clickButton(self):
        self.driver.find_element_by_link_text(self.sort_by_link_text).click();