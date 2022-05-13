#!/usr/bin/python

import os
import sys
import credentials
from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def Switch_IP():
    os.system("protonvpn-cli status")
    os.system("protonvpn-cli c -r")
    os.system("protonvpn-cli status")

#Switch_IP()

# open chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# login to a Linkedin account
def Login():
    # go to linkedin
    driver.get('https://www.linkedin.com')
    # select username input
    username = driver.find_element(by=By.CLASS_NAME, value='input__input')
    # write username input
    username.send_keys(credentials.linkedin_email)
    # select password input
    password = driver.find_element(by=By.ID, value='session_password')
    # write password input
    password.send_keys(credentials.linkedin_pass)
    # log in
    log_in_button = driver.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button') 
    log_in_button.click()

Login()


arg1 = sys.argv[1]
arg2 = sys.argv[2]

people = ['people', 'People', 'PEOPLE', 'persons']
companies = ['company', 'companies', 'Companies', 'COMPANIES']

if any(x in arg1 for x in people):
    for i in range(1,3):
        driver.get('https://www.linkedin.com/search/results/people/?keywords='+arg2+'&page='+str(i))
        sleep(3)
elif any(x in arg1 for x in companies):
    for i in range(1,100):
        driver.get('https://www.linkedin.com/search/results/companies/?keywords='+arg2+'&page='+str(i))
        sleep(3)
else: print('wrong arguments!')
