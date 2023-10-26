from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your own username and password
username = "Your_Username"
password = "Your_Password"

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open Instagram
driver.get("https://www.instagram.com/")
time.sleep(2)

# Locate the username and password fields, and input the login credentials
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")

username_input.send_keys(username)
password_input.send_keys(password)

# Simulate pressing the enter key
password_input.send_keys(Keys.RETURN)
time.sleep(3)

# Once logged in, like posts on the homepage
for i in range(5):  # Replace 5 with the desired number of posts to like
    try:
        # Locate the like button and click it
        like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]')
        like_button.click()
        time.sleep(2)
    except Exception as e:
        print(e)
    # Move to the next post
    driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
    time.sleep(2)

# Close the browser
driver.close()
