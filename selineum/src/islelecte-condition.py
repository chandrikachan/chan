'''
Created on 21-Feb-2023

@author: Karthik
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import Select
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver._switch_to.frame("frame-one1434677811")
radio_button=driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-7_1']")
status=radio_button.is_selected()
print(status)
radio_button.click()
time.sleep(2)
status2=radio_button.is_selected()
print("radio button is clicked")
print(status2)
check_box=driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_1']")
#check_box.click()
status_checkbox=check_box.is_enabled()
print(status_checkbox)