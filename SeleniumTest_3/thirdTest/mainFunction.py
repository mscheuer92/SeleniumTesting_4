from selenium import webdriver
import unittest
from searchObject import SearchObject
from sortPrice import SortPrice
from selectItem import SelectItem
from addToCart import AddtoCart
from insideCart import InsideCart

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
  
        sort = SortPrice(driver)
        sort.clickButton()
        
        select = SelectItem(driver)
        select.clickItem()
      
        add = AddtoCart(driver)
        add.checkQuantity("//*[@id='qtySubTxt']/span")
        add.addToCart()
        add.goToCart()
        
        remove = InsideCart(driver)
        remove.removeItem()
       
   
      
        
    
    
    
    
    
    if __name__ == "__main__":
            unittest.main()