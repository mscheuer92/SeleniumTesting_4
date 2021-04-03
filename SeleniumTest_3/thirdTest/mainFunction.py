from selenium import webdriver
import unittest
from searchObject import SearchObject
#from objectPage import ObjectPage

class mainFunction (unittest.TestCase):
   
    def setUp(self):
        self.driver =  webdriver.Chrome(executable_path='/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.ebay.com")
        title = self.driver.title
        self.assertEqual ("Electronics, Cars, Fashion, Collectibles & More | eBay", title, "Title does not match")
     
    def test_Navigation(self):
        driver = self.driver
        
        search = SearchObject(driver)
        search.enter_itemSearch("coffee")
        search.click_Button()
  
        #checkbox = ObjectPage(driver)
        #checkbox.click_checkbox()
        
   
        
    if __name__ == "__main__":
            unittest.main()