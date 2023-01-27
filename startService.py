from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time

def document_initialised(driver):
    return driver.execute_script("return initialised")
    
options = Options()
options.add_argument("--disable-notifications")

''' under Windows Environment '''
## driver = webdriver.Chrome("./win_webdriver/chromedriver")
''' under Mac_ARM Environment '''
chrome = webdriver.Chrome("/chromedriver")
''' under Linux Environment '''
## driver = webdriver.Chrome("./linux_webdriver/chromedriver")

chrome.get("https://mtr_advpanel_mmi.rocteccloud.com/#/Login")
chrome.implicitly_wait(3)

userName = chrome.find_element(By.ID, 'userNameInput')
passWord = chrome.find_element(By.ID, 'outlined-adornment-password')
loginButton = chrome.find_element(By.ID, 'loginButton')

userName.send_keys('duat-mtriecc')
passWord.send_keys('P@ssw0rd')

loginButton.click()

time.sleep(5)
'''
chrome.get('https://mtr_advpanel_mmi.rocteccloud.com/#/Overview')
time.sleep(5)

tableHeaders = chrome.find_elements(By.CLASS_NAME, 'css-cc8tf1')

for e in tableHeaders:
    print(e.text)

print('####################################')

tableRows = chrome.find_elements(By.CLASS_NAME, 'css-1inm7gi')
records = tableRows.split()
tableSVG = chrome.find_elements(By.CLASS_NAME, 'css-vubbuv')
for e in tableSVG:
    print(e.get_attribute('path'))
'''
soup = BeautifulSoup(chrome.page_source, 'html.parser')
print(soup)