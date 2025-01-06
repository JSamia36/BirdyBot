from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import pickle, time, random, pyperclip, re
from selenium.webdriver import ActionChains
import subprocess

print("Tweeting will have to wait until after this nap")
print("Rise and shine, tweeting time")
driver_path = 'chromedriver'  
service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://twitter.com') 
wait = WebDriverWait(driver, 10)
filename = 'file.txt'

# ----- importing cookies -----
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)

driver.get('https://twitter.com/compose/post')

post = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-autocomplete=list]'))
)

# ----- Choosing random thing to send -----
with open(filename) as file:
    lines = file.read().splitlines()

chosen_lines = random.choice(lines)
print(chosen_lines) 

with open(filename, 'w') as output_file:
    output_file.writelines(line + "\n" for line in lines if line not in chosen_lines)

tweet_box = 'div[aria-autocomplete="list"]'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, tweet_box))
)
tBox = driver.find_element(By.CSS_SELECTOR, tweet_box)
tBox.click()

def copy_image(image_path):
    subprocess.run(["xclip", "-selection", "clipboard", "-t", "image/png", "-i", image_path])

if '<' and '>' in chosen_lines:
    remSym = re.search('<(.*)>', chosen_lines)
    imagePath = (remSym.group(1))
    
    twt = re.sub('<.*?>', '', chosen_lines)
    copy_image(image_path)

    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    pyperclip.copy(twt)
    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

else:
    pyperclip.copy(chosen_lines)
    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


# Post submit
postButton = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetButton']"))
 )
postButton.click()

driver.quit()
print("Tweeting went well!")
