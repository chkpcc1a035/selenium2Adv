from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--disable-notifications")

''' under Windows Environment '''
## driver = webdriver.Chrome("./win_webdriver/chromedriver")
''' under Mac_ARM Environment '''
chrome = webdriver.Chrome("/chromedriver")
''' under Linux Environment '''
## driver = webdriver.Chrome("./linux_webdriver/chromedriver")

chrome.get("https://mtr_advpanel_mmi.rocteccloud.com/#/Login")
userName = chrome.find_element(By.ID, 'userNameInput')
passWord = chrome.find_element(By.ID, 'outlined-adornment-password')
loginButton = chrome.find_element(By.ID, 'loginButton')

userName.send_keys('duat-mtriecc')
passWord.send_keys('P@ssw0rd')

loginButton.click()

time.sleep(7)
chrome.get('https://mtr_advpanel_mmi.rocteccloud.com/#/Alarms!')
time.sleep(10)