class myoduPage():
    
    def __init__(self,driver):
        self.driver = driver
        self.login_by_class_name = 'fa-sign-in'
       
    def clickLogin(self):
        self.driver.find_element_by_class_name(self.login_by_class_name).click()
