
class SearchObject():
    
    def __init__(self,driver):
        self.driver = driver
        self.searchbar_by_name = "_nkw"
        self.click_button_by_id = 'gh-btn'
        
    def enter_itemSearch(self, _nkw):
        self.driver.find_element_by_name(self.searchbar_by_name).send_keys(_nkw)
            
    def click_Button(self):
        self.driver.find_element_by_id(self.click_button_by_id).click()
    
        