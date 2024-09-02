import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "Admin" # Use your Login ID and Password
PASSWORD = "Admin@123"


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(10)
        save_info = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        save_info.click()
        time.sleep(2)
        notification = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        notification.click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps/')
        time.sleep(5)
        follower_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, value=' followers')
        follower_button.click()
        time.sleep(5)
        timeout = time.time() + 20
        while time.time() < timeout:
            time.sleep(5)
            scr1 = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

    def follow(self):
        i = 1
        while True:
            follow_button = self.driver.find_element(By.XPATH, value=f'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button')
            follow_button.click()
            i += 1
            time.sleep(2.5)




call_instagram = InstaFollower()
login = call_instagram.login()
find_followers = call_instagram.find_followers()
follow = call_instagram.follow()