from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from time import perf_counter
from bs4 import BeautifulSoup
import time
import json
import requests

class AdvSenleniumService():

    processStart = perf_counter()
    chromiumService = Service(r'./linux_webdriver/chromedriver109')

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage') 
    ''' under Windows Environment '''
    chrome = webdriver.Chrome(service=chromiumService, options=options)
    ''' under Mac_ARM Environment '''
    # chrome = webdriver.Chrome(service=chromiumService, options=options)
    ''' under Linux Environment '''
    # chrome = webdriver.Chrome(service=chromiumService, options=options)

    chrome.set_window_size(4096, 4096)
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
    chrome.get('https://mtr_advpanel_mmi.rocteccloud.com/#/Overview')
    time.sleep(5)
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    tableTitles = soup.find_all(
        'div', {'class': 'MuiDataGrid-columnHeaderTitle css-cc8tf1'})
    i = 0
    tempTitleDict = {}
    tempRows = {}
    tempHealth = []

    for tableTitle in tableTitles:
        tempTitleDict.update({tableTitles.index(tableTitle): tableTitle.text})

    tableRows = soup.find_all('div', {'class': 'MuiDataGrid-cellContent'})
    for tableRow in tableRows:
        tempRows.update({tableRows.index(tableRow): tableRow.text})

    healthRecords = soup.find_all('svg', attrs={'class': 'MuiSvgIcon-root MuiSvgIcon-fontSizeMedium islockedDeviceStatus css-vubbuv'})
    for healthRecord in healthRecords:
        if healthRecord.has_attr('style'):
            tempHealth.append(False)
        else:
            tempHealth.append(True)

    processEnd = perf_counter()
    advRecords = {'header': tempTitleDict, 'rowsText': tempRows, 'healthStatus': tempHealth}
    
    print(json.dumps(advRecords))

    # res = requests.post('', json = json.dumps(advRecords))

    print('Elapsed Time in seconds: ', processEnd - processStart)