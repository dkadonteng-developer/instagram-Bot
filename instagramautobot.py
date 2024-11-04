from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "Your_Username"
password = "Your_Password"

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")
time.sleep(2)

username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")

username_input.send_keys(username)
password_input.send_keys(password)

password_input.send_keys(Keys.RETURN)
time.sleep(3)

for i in range(5):  
    try:
        like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]')
        like_button.click()
        time.sleep(2)
    except Exception as e:
        print(e)
    driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
    time.sleep(2)

driver.close()
