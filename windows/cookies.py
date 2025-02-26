from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
import pickle, yaml

driver_path = 'chromedriver.exe'  
service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://twitter.com/i/flow/login') 
wait = WebDriverWait(driver, 10)

with open ("config.yaml") as configFile:
    config = yaml.safe_load(configFile)

userLogon = config['login']['username']
userPass = config['login']['password']

# ------ LOGGING IN ------
username = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
)
username.send_keys(userLogon)

login_button = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
)
login_button.click()

password = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[type=password]'))
)
password.send_keys(userPass)

login_button = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
)
login_button.click()

direct_message_link = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=AppTabBar_DirectMessage_Link]'))
)

pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

driver.quit()
