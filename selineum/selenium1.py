from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://google.com")#to test google page to gmail
driver.find_element(By.XPATH,"//*[@id='gb']/div/div[1]/div/div[1]/a").click()


#to test google to gmail page by closing no thanks window
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
driver.switch_to.frame("callout")
driver.find_element(By.XPATH,"//button[@aria-label='No thanks']").click()
time.sleep(5)
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,".//a[@class='gb_p' and @aria-label='Gmail (opens a new tab)']").click()


#to test google to sign in directly
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame("callout")
no_Thanks=driver.find_element(By.XPATH,"//button[@aria-label='No thanks']")
no_Thanks.click()
time.sleep(2)
driver.switch_to.parent_frame()
gmail=driver.find_element(By.XPATH,".//a[@class='gb_p' and @aria-label='Gmail (opens a new tab)']")
gmail.click()
sign_in=driver.find_element(By.XPATH,"//a[@data-action='sign in']")
sign_in.click()
#driver.switch_to.parent_frame()
email=driver.find_element(By.XPATH,"//input[@type='email']")
email.send_keys("chethanachandrika@gmail.com")
#driver.switch_to.parent_frame()
action.click