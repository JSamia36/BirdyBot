from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
import pickle, time, yaml, random
from selenium.webdriver.support import expected_conditions as EC

with open('config.yaml') as configFile:
    config = yaml.safe_load(configFile)

RetweetMin = config['retweet_timer']['retweet_min']
RetweetMax = config['retweet_timer']['retweet_max']

RCN = config['retweet_amount']['retweet_min']
RCX = config['retweet_amount']['retweet_max']

retweetTGT = config['theme']['querySearch']

print("retweeting soon")
time.sleep((random.randint(RetweetMin,RetweetMax)))
print("finally going to retweet")
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

driver.get(f'https://twitter.com/search?q={retweetTGT}&src=typed_query') 
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

retweet_button = driver.find_elements(By.CSS_SELECTOR, "[data-testid='retweet']")

randSleep = random.randint(1,15)
skipNum = random.choice(['on', 'off', 'on']) # if off skip tweet, if not retweet that tweet
Num2RT = random.randint(RCN,RCX)
time.sleep(10)
for button in retweet_button[:Num2RT]:
    if skipNum == 'on':
        try:
            button.click()
            time.sleep(10)
            retweet_confirm = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='retweetConfirm']"))
            )
            retweet_confirm.click()
            time.sleep(10)
            time.sleep(randSleep)
        except:
            continue
    else:
        continue

print('Finished')
