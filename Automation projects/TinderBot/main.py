from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

# LOGIN SETUP
time.sleep(3)
log_in = driver.find_element(By.XPATH, value='//*[@id="c1323653706"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()

time.sleep(2)
more_option = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
more_option.click()

time.sleep(2)
facebook_login = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_login.click()


# FACEBOOK LOGIN
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)

# Use your own login and password of Tinder
email = "Admin"
password = "admin@123"

time.sleep(2)
email_add = driver.find_element(By.XPATH, value='//*[@id="email"]')
email_add.send_keys(email)
pass_add = driver.find_element(By.XPATH, value='//*[@id="pass"]')
pass_add.send_keys(password, Keys.ENTER)

time.sleep(2)
driver.switch_to.window(base_window)

time.sleep(2)
cookie = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie.click()

# time.sleep(1)
# location = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div[1]/div/div/div[3]/button[1]')
# location.click()

time.sleep(1)
notification = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div/div/div/div[3]/button[2]')
notification.click()

time.sleep(5)
while True:
    dislike = driver.find_element(By.XPATH, value='//*[@id="c1323653706"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
    dislike.click()
    time.sleep(2)