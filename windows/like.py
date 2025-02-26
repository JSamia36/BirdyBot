from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
import pickle, time, yaml, random

with open('config.yaml') as configFile:
    config = yaml.safe_load(configFile)

LikeMin = config['like_timer']['like_min']
LikeMax = config['like_timer']['like_max']

LCN = config['like_amount']['like_min']
LCX = config['like_amount']['like_max']

likeTGT = config['theme']['querySearch']

print("going to send some likes after this nap")
time.sleep((random.randint(LikeMin,LikeMax)))
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

driver.get(f'https://twitter.com/search?q={likeTGT}&src=typed_query&f=live') # CHANGE CRYPTO TO SEARCH YOU WANT
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

like_button = driver.find_elements(By.CSS_SELECTOR, "[data-testid='like']")

randSleep = random.randint(2,15)
skipNum = random.choice(['on', 'off', 'on']) # if off skip tweet, if not like that tweet
Num2Like = random.randint(LCN,LCX)

for button in like_button[:Num2Like]: 
    if skipNum == 'on':
        try:
            button.click()
            time.sleep(randSleep)
        except:
            continue
    else:
        continue

driver.quit()
print('Sent the likes :)')
