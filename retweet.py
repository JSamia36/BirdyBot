import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
import pickle, time, os, random

time.sleep((random.randint(60,1800)))
driver_path = 'chromedriver.exe'  
service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://twitter.com') 
wait = WebDriverWait(driver, 10)

# ----- importing cookies -----
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)

driver.get('https://twitter.com/search?q=crypto&src=typed_query&f=live') # for liking
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

like_button = driver.find_elements(By.CSS_SELECTOR, "[data-testid='retweet']")

randSleep = random.randint(1,15)
skipNum = random.choice(['on', 'off', 'on']) # if off skip tweet, if not retweet that tweet
Num2Like = random.randint(0,3)

for button in like_button[:Num2Like]: # Retweet 3 tweets, adjust as desired
    if skipNum == 'on':
        try:
            button.click()
            time.sleep(randSleep)
        except:
            continue
    else:
        continue

print('Success')