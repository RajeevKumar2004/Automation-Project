from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 21.21
PROMISED_UP = 7.3


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        cookie = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        cookie.click()
        start = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start.click()
        time.sleep(60)
        down_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return down_speed, up_speed

    def tweet_at_provider(self, speed):
        self.driver.get("https://twitter.com/i/flow/signup")
        time.sleep(5)
        login = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/button')
        login.click()
        time.sleep(5)
        signin_email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        signin_email.send_keys("Admin", Keys.ENTER)#Use your twiter Login mail
        time.sleep(2)
        signin_pass = self.driver.find_element(By.NAME, value='password')
        signin_pass.send_keys("Admin@123", Keys.ENTER)#USe your password
        time.sleep(5)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        post_button.click()
        if float(speed[0]) != PROMISED_DOWN or float(speed[1]) != PROMISED_UP:
            time.sleep(2)
            post = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
            post.send_keys(f"@JioCare @JioCare Hey Internet provider, why is my internet speed {speed[0]}down/{speed[1]}up when average speed is {PROMISED_DOWN}down/{PROMISED_UP}up?")
            send = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
            send.click()
        return 1
