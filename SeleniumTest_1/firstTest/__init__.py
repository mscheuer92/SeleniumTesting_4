from selenium import webdriver
import unittest
import HtmlTestRunner


class googleSearch(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver')
        cls.driver.maximize_window()

    def test_searchOnPage(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Michelle Scheuer")
        self.driver.find_element_by_name("btnK").click()
        self.driver.find_element_by_partial_link_text('Software Support Engineer').click()
        print("I am looking for a job :)")
  
    @classmethod
    def loadpageClass(cls):
        cls.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("This test is now complete.")
        
    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output ='/home/michelle/Desktop/Selenium/Python_HtmlReport'))