from selenium import webdriver
import unittest
from HomePage import homePage
from LoginPage import loginPage
from myOduPage import myoduPage


class main(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver')
        cls.driver.implicitly_wait(10)
        #cls.driver.maximize_window()
        
    def test_navigate(self):
        driver = self.driver
        driver.get("https://www.odu.edu")
        
        home = homePage(driver)
        home.clicklink();
     
        myOdu = myoduPage(driver)
        myOdu.clickLogin()
        
        login = loginPage(driver)
        login.enter_username("not-a-username")
        login.enter_password("not-a-password")
        login.clickLogin()
     
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Testcomplete")
