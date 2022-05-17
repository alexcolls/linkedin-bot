#!/usr/bin/python

from csv import reader
import time
from login import Login
from login import driver
from selenium.webdriver.common.by import By
import random

name = input('\nInsert name of the database... ')
db = open(name+'.csv')
data = list(reader(db))

Login()

def Connect():
    try:

        time.sleep(3)
        send_button = driver.find_element(by=By.ID, value='ember264') 
        send_button.click()
    except:
        menu_button = driver.find_element(by=By.ID, value='ember67') 
        menu_button.click()
        time.sleep(3)
        connect_button = driver.find_element(by=By.ID, value='ember73') 
        connect_button.click()
        time.sleep(3)
        send_button = driver.find_element(by=By.ID, value='ember264') 
        send_button.click()
    else: 
        print('Already connected!')

connect_button = driver.find_element(by=By.CLASS_NAME, value='pvs-profile-actions ')

connect_button = driver.find_element(by=By.CLASS_NAME, value='pvs-profile-actions__action')

connect_button.click()


driver.get(data[12][0])


Connect()

for profile in data:
    print(profile[0]+'...')
    driver.get(profile[0])
    time.sleep(3)
    Connect()
    ranint = random.randint(10,25)
    print('Sleeping '+str(ranint)+' seconds...')
    time.sleep(ranint)
