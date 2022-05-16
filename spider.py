#!/usr/bin/python

from ast import Pass
import os
from csv import reader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import credentials
import random
import bs4 as bs

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





def Scroll():
    start = time.time()
    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000
    while True:
        driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
        # this command scrolls the window starting from
        # the pixel value stored in the initialScroll 
        # variable to the pixel value stored at the
        # finalScroll variable
        initialScroll = finalScroll
        finalScroll += 1000
        # we will stop the script for 3 seconds so that 
        # the data can load
        time.sleep(3)
        # You can change it as per your needs and internet speed
        end = time.time()
        # We will scroll for 20 seconds.
        # You can change it as per your needs and internet speed
        if round(end - start) > 20:
            break


for profile in data:
    print(profile[0]+'...')
    driver.get(profile[0])
    #SwitchIP()
    ranint = random.randint(10,25)
    print('Sleeping '+str(ranint)+' seconds...')
    time.sleep(ranint)

driver.get(data[1][0])
Scroll()

driver.execute_script("return document.documentElement.outerHTML")

html = driver.page_source
soup = bs(html)            

def Name():
    name = ''
    try:
        name = soup.find('h1').get_text()
    except: pass
    return name

def Title():
    title = ''
    try:
        title = soup.find('div', class_='text-body-medium break-words').get_text()
        title = title.replace('\n      ', '')
        title = title.replace('\n    ', '')
    except: pass
    return title

def Company():
    company = ''
    try:
        company = soup.find('h2', class_='pv-text-details__right-panel-item-text hoverable-link-text break-words text-body-small inline').get_text()
        company = company.replace('\n\n\n    ', '')
        company = company.replace('\n  \n\n', '')
    except: pass
    return company

def Location():
    location = ''
    try:
        location = soup.find('span', class_='text-body-small inline t-black--light break-words').get_text()
        location = location.replace('\n      ', '')
        location = location.replace('\n    ', '')
    except: pass
    return location

def About():
    about = ''
    try:
        about = soup.find('div', class_='pv-shared-text-with-see-more t-14 t-normal t-black display-flex align-items-center').find('span').get_text()
    except: pass
    return about

def Followers():
    followers = 0
    try:
        followers = soup.find('p', class_='pvs-header__subtitle text-body-small').find('span').get_text()
        followers = int(followers.replace(' followers', ''))
    except: pass
    return followers

# contact

driver.get('https://www.linkedin.com'+str(soup.find('a', id='top-card-text-details-contact-info').get('href')))


soup.find('div', class_='display-flex flex-column full-width align-self-center')

soup.find('section', id='ember62').find_all('span')
a_tags = li_tags.find("a")
job_title = a_tags.find("h3").get_text().strip()
  
print(job_title)