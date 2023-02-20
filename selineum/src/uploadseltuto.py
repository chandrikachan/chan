from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")
driver.execute_script("window.scrollby(0,900)","")
driver.execute_to_frame("frame-one1434677811")
upload=driver.find_element(By.XPATH,"//input[@id='RESULT_FileUpload-10']")  
upload.send_keys(r"C:\Users\91636\Desktop\chandika s resume1.pdf") 
action=ActionChains(driver)    
