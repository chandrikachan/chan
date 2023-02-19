from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")#to use in private browser
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://shorturl.at/luLV6")
# click_me=driver.find_element(By.ID,"landingImage")#one type double clicks the image
# action=ActionChains(driver)
# action.double_click(click_me).perform()
img=driver.find_element(By.ID,"landingImage")#another type goes to only image
action=ActionChains(driver)
action.move_to_element(img).perform()