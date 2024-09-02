import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
data = response.text


# Scraping using_wtf BEAUTIFULSOUP
soup = BeautifulSoup(data, "html.parser")

# Price of property
price = []
house = soup.findAll(name="div", class_='PropertyCardWrapper')
for i in house:
    house_rent = i.text.split()[0].split('/')[0].split('+')[0]
    price.append(house_rent)

# Addresses of property
addresses = []
address = soup.findAll(name="address")
for i in address:
    house_address = i.text.strip()
    addresses.append(house_address)

# Link to property
links = []
link = soup.findAll(name="a", class_="property-card-link")
for i in link:
    property_link = i.get("href")
    links.append(property_link)


# DATA ENTRY using_wtf SELENIUM
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/EkbKJbXYJ6QkKRzA6")
driver.maximize_window()
time.sleep(5)
for i in range(0, len(addresses)):
    time.sleep(2)
    add_entry = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_entry.send_keys(addresses[i])
    price_entry = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_entry.send_keys(price[i])
    link_entry = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry.send_keys(links[i])
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    time.sleep(2)
    another_form = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_form.click()
