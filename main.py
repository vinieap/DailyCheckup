from selenium import webdriver
import pickle
import os.path
from os import path
import time
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import getpass

# Open secret.txt file for username and password information

if not path.exists('secret.txt'):
    os.mknod('secret.txt')
    f = open("secret.txt", "w")
    f.write(getpass.getpass("eid: ") + "\n")
    f.write(getpass.getpass("password: "))
    f.close()

f = open("secret.txt", "r")

user = f.readline()
pwd = f.readline()

f.close()

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

wait = WebDriverWait(driver, 5)

driver.get("https://dailyhealth.vcu.edu/")

# if path.exists("cookies.pkl"):
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         driver.add_cookie(cookie)
# 
# driver.get("https://dailyhealth.vcu.edu/")

driver.find_element_by_xpath('//*[@id="username"]').send_keys(user)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
button = driver.find_element_by_xpath('//*[@id="fm1"]/div[3]/button')
button.click()

try:
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="no"]')))
    driver.execute_script("document.getElementById('no').style.display='inline-block';")
    button = driver.find_element_by_xpath('//*[@id="no"]')
    button.click()
    driver.execute_script("document.getElementById('daily-health-submit').style.display='inline-block';")
    button = driver.find_element_by_xpath('//*[@id="daily-health-submit"]')
    button.click()
    print('Checkup Done for: {}'.format(datetime.today().strftime('%m-%d-%Y')))
except TimeoutException:
    print("Already Done")

# if not path.exists("cookies.pkl"):
#     pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

driver.quit()