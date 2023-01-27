from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from time import perf_counter
from bs4 import BeautifulSoup
import time
import json


class AdvSenleniumService():

    processStart = perf_counter()
    chromiumService = Service(r'/chromedriver')

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    ''' under Windows Environment '''
    # chrome = webdriver.Chrome("./win_webdriver/chromedriver")
    ''' under Mac_ARM Environment '''
    chrome = webdriver.Chrome(service=chromiumService, options=options)
    chrome.set_window_size(4096, 4096)
    ''' under Linux Environment '''
    # chrome = webdriver.Chrome("./linux_webdriver/chromedriver")
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

    tempTitleDict = {}
    tempRows = {}
    tempHealth = {}
    for tableTitle in tableTitles:
        print('-------------------------------[Header]')
        print(tableTitle.text)
        tempTitleDict.update({tableTitles.index(tableTitle): tableTitle.text})

    tableRows = soup.find_all('div', {'class': 'MuiDataGrid-cellContent'})
    for tableRow in tableRows:
        print('-------------------------------[Row]')
        print(tableRow.text)
        tempRows.update({tableRows.index(tableRow): tableRow.text})

    healthRecords = soup.find_all('path', attrs={'d': 'M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2z'})
    for healthRecord in healthRecords:
        i = 0
        print('-------------------------------[Health]')
        print('GOOD')
        tempHealth.update({ i : True})
        i + 1

    processEnd = perf_counter()
    advRecords = {'header': tempTitleDict, 'rowsText': tempRows, 'healthStatus': tempHealth}
    
    print(advRecords)

    print('Elapsed Time in seconds: ', processEnd - processStart)