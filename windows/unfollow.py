from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
import pickle, time, random, yaml
from selenium.webdriver.support import expected_conditions as EC

with open('config.yaml') as configFile:
    config = yaml.safe_load(configFile)

FollowMin = config['follow_timer']['follow_min']
FollowMax = config['follow_timer']['follow_max']

FCN = config['follow_amount']['follow_min']
FCX = config['follow_amount']['follow_max']

username = config['login']['username']
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

driver.get(f'https://x.com/{username}/following') # your username for unfollowing
time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

follow_button = driver.find_elements(By.CSS_SELECTOR, "button[data-testid$='unfollow']")


randSleep = random.randint(1,17)
Num2Follow = random.randint(FCN,FCX) # There is a 400 a day limit for non verified accounts

for button in follow_button[:Num2Follow]: 
    try:
        button.click()
        time.sleep(2)
        conButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='confirmationSheetConfirm']")))
        conButton.click()
        time.sleep(randSleep)
    except:
        continue
    continue


print("Unfollowed some old friends")
