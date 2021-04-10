from selenium import webdriver
import unittest
from homepage import HomePage

class testWex(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver')
        #cls.driver.maximize_window()
    
    def test_pageNavigation(self):
        self.driver.get("https://wexinc.com")
        title = self.driver.title
        self.assertEqual("Game-changing payment solutions for every business | WEX Inc.", title, "The titles don't match")
        
        driver = self.driver
        hometest = HomePage(driver)
       
        
        
        
    if __name__ == "__main__":
            unittest.main()