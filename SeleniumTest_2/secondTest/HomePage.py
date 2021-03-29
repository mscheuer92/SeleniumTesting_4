class homePage():
    
    def __init__(self,driver):
        self.driver = driver
        self.myodu_link_class = "fa-users"
        
    def clicklink(self):
        self.driver.find_element_by_class_name(self.myodu_link_class).click()


    