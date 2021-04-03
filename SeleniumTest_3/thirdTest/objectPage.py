class ObjectPage():
    
    def __init__(self,driver):
        self.driver = driver
        self.click_item_by_xpath = "//div[@id='srp-river-results']/ul/li[6]/div/div[2]/a/h3"
        
    def click_checkbox(self):
        self.driver.find_element_by_xpath(self.click_checkbox()).click()