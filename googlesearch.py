import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def test_search_google(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
    def test_search_me(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Akshatha Shivanna instagram")
        self.driver.find_element_by_name("btnK").click()
    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("test completed")
if __name__ == "__main__":
	unittest.main(argv=['first-arg-is-ignored'], exit=False) 
