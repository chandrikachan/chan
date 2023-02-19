from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")
upload=driver.find_element(By.ID,"RESULT_FileUpload-10")
driver.execute_script("arguments[0].scrollIntoView();",upload)  
action=ActionChains(driver)  
upload.click()     