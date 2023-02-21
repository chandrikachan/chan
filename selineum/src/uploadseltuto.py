from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains
#import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,900)","")
driver.switch_to.frame("frame-one1434677811")
#driver.find_element(By.XPATH,".//input[@name='RESULT_TextField-1']").send_keys("asha")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
upload=driver.find_element(By.XPATH,".//input[@id='RESULT_FileUpload-10']")
upload.send_keys(r"C:\Users\91636\Desktop\chandika s resume1.pdf")
#action=ActionChains(driver)
#action.click(photo).perform()