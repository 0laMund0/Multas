#import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def setUp(self):
    self.driver = webdriver.Firefox()

def test_search_in_python_org(self):
    driver = self.driver
    driver.get("http://www.python.org")
    self.assertIn("Python", driver.title)
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    #self.assertNotIn("No results found.", driver.page_source)