from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
resizable=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']",)
action=ActionChains(driver)
action.click_and_hold(resizable).move_by_offset(200,0).perform()
