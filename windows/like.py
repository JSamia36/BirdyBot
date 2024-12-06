from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
import pickle, time, yaml, random

with open('config.yaml') as configFile:
    config = yaml.save_load(configFile)

FollowMin = config['follow_timer']['follow_min']
FollowMax = config['follow_timer']['follow_max']

FCN = config['follow_amount']['follow_min']
FCX = config['follow_amount']['follow_max']

print("going to send some likes after this nap")
time.sleep((random.randint(FollowMin,FollowMax)))
print("nap finished, sending those likes now")
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

driver.get('https://twitter.com/search?q=crypto&src=typed_query&f=live') # CHANGE CRYPTO TO SEARCH YOU WANT
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

like_button = driver.find_elements(By.CSS_SELECTOR, "[data-testid='like']")

randSleep = random.randint(2,15)
skipNum = random.choice(['on', 'off', 'on']) # if off skip tweet, if not like that tweet
Num2Like = random.randint(FCN,FCX)

for button in like_button[:Num2Like]: 
    if skipNum == 'on':
        try:
            button.click()
            time.sleep(randSleep)
        except:
            continue
    else:
        continue

print('Sent the likes :)')
