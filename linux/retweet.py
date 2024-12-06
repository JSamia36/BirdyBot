from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
import pickle, time, yaml, random

with open('config.yaml') as configFile:
    config = yaml.save_load(configFile)

RetweetMin = config['retweet_timer']['retweet_min']
RetweetMax = config['retweet_timer']['retweet_max']

RCN = config['retweet_amount']['retweet_min']
RCX = config['retweet_amount']['retweet_max']

print("retweeting soon")
time.sleep((random.randint(RetweetMin,RetweetMax)))
print("finally going to retweet")
driver_path = 'chromedriver'  
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

driver.get('https://twitter.com/search?q=crypto&src=typed_query') 
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

like_button = driver.find_elements(By.CSS_SELECTOR, "[data-testid='retweet']")

randSleep = random.randint(1,15)
skipNum = random.choice(['on', 'off', 'on']) # if off skip tweet, if not retweet that tweet
Num2Like = random.randint(RCN,RCX)

for button in like_button[:3]:
    if skipNum == 'on':
        try:
            button.click()
            time.sleep(randSleep)
        except:
            continue
    else:
        continue

print('Retweet Success')
