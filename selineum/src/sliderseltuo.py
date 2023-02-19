from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
slider=driver.find_element(By.XPATH,"//span[@tabindex='0']")
action=ActionChains(driver)
action.click_and_hold(slider).move_by_offset(100,0).perform()


