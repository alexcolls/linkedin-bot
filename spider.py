#!/usr/bin/python

import os
from csv import reader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import credentials
import random


name = input('\nInsert name of the database... ')
db = open(name+'.csv')
data = list(reader(db))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def Login():
    # go to linkedin
    driver.get('https://www.linkedin.com')
    # select username input
    username = driver.find_element(by=By.CLASS_NAME, value='input__input')
    username.send_keys(credentials.linkedin_email) #'krystnft@gmail.com'
    # select password input
    password = driver.find_element(by=By.ID, value='session_password')
    password.send_keys(credentials.linkedin_pass) #'&HackMe&...'
    # log in
    log_in_button = driver.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button') 
    log_in_button.click()

os.system("protonvpn-cli d")
Login()
sleep(20)

def SwitchIP():
    os.system("protonvpn-cli c -r")
    os.system("protonvpn-cli status")


SwitchIP()

for profile in data:
    print(profile[0]+'...')
    driver.get(profile[0])
    #SwitchIP()
    ranint = random.randint(10,25)
    print('Sleeping '+str(ranint)+' seconds...')
    sleep(ranint)


driver.get(data[0][0])
html = driver.page_source


"""

from bs4 import BeautifulSoup as bs

soup = bs(html)                #make BeautifulSoup
prettyHTML = soup.prettify()

soup.findAll('div')

name = soup.find('h1').get_text()

description = soup.find('div', class_='text-body-medium break-words').get_text()
description = description.replace('\n      ', '')
description = description.replace('\n    ', '')

location = soup.find('span', class_='text-body-small inline t-black--light break-words').get_text()
location = location.replace('\n      ', '')
location = location.replace('\n    ', '')

soup.find('p', class_='pvs-header__title-container')

"""
