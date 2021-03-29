class loginPage():
    
    def __init__(self,driver):
        self.driver = driver
        self.username_by_id = "username"
        self.password_by_id = "password"
        self.login_by_name = "_eventId_proceed"
        
    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_by_id).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_by_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element_by_name(self.login_by_name).click()