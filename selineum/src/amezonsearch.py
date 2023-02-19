from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://amazon.com")
data=driver.find_element(By.XPATH,"//input[@type='text'and @dir='auto']")
data.send_keys("mobiles")
send=driver.find_element(By.XPATH,"//input[@type='submit']")
send.click()
