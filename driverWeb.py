from selenium import webdriver
#driver = webdriver.Chrome('/home/user/drivers/chromedriver')
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get("http://www.google.com")
#assert "Python" in driver.title
#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("filósofo pycão")
#elem.send_keys(Keys.RETURN)

