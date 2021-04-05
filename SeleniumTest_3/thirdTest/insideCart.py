#5th page. Inside cart. Remove item that was added

class InsideCart():

    def __init__(self,driver):
        self.driver = driver
        self.driver.removeitemby_xpath = "(//button[@type='button'])[2]"
    
    def removeItem(self):
        self.driver.find_element_by_xpath(self.driver.removeitemby_xpath).click()
        self.driver.implicitly_wait(20)