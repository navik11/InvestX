import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

driver = webdriver.Chrome()
url = "https://sso.definedge.com/auth/realms/definedge/protocol/openid-connect/auth?response_type=code&client_id=opstra&redirect_uri=https://opstra.definedge.com/ssologin&state=e2cf559f-356c-425a-87e3-032097f643d0&login=true&scope=openid"

driver.get(url)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("navik09.me@gmail.com")
password.send_keys("j5mn66s7@OPSTRA")

loginBtn = driver.find_element(By.ID, "kc-login")
loginBtn.click()

driver.get('https://opstra.definedge.com/strategy-builder')
time.sleep(.5)
expander = driver.find_element(By.CLASS_NAME, 'v-expansion-panel__header__icon')
expander.click()
time.sleep(.5)

dates = driver.find_elements(By.CSS_SELECTOR, '.flex.xs4.sm2.md1')
lens = len(dates)
for i in range(0, lens):
    dates = driver.find_elements(By.CSS_SELECTOR, '.flex.xs4.sm2.md1')
    dates[i].click()
    # fetchdata(f'{i}_{dates[i].text}')
    time.sleep(2)
    html_code = driver.page_source
    # print(html_code.encode('ascii', 'ignore').decode('ascii'))
    soup = BeautifulSoup(html_code, 'html.parser')
    table = soup.find('table', class_="v-datatable")

    df = pd.read_html(str(table))[0]
    df.to_csv(f'{i}_{dates[i].text}'+".csv", index=False)