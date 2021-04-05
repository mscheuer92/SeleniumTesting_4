#3rd page. Selecting "Folgers Classic Roast Ground Coffee"

class SelectItem():
    
    def __init__(self, driver):
        self.driver = driver
        self.selectitem_by_link_text = "Folgers Classic Roast Ground Coffee (51 oz.) FREE SHIPPING"
    
        
    def clickItem(self):
        self.driver.find_element_by_link_text(self.selectitem_by_link_text).click()