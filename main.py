# import libraries
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from time import sleep
import credentials
import numpy as np


# open chrome driver
def Driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = Driver()

# login to a Linkedin account
def Login():
    # go to linkedin
    driver.get('https://www.linkedin.com')
    # select username input
    username = driver.find_element(by=By.CLASS_NAME, value='input__input')
    # email input
    email = input('\nIntroduce a Linkedin email or press enter for default: ')
    if len(email) < 4:
        email = credentials.linkedin_email
    # write username input
    username.send_keys(email)
    # select password input
    password = driver.find_element(by=By.ID, value='session_password')
    # password input
    getpassword = getpass('Introduce password: ')
    if len(getpassword) < 4:
        getpassword = credentials.linkedin_pass
    # write password input
    password.send_keys(getpassword)
    # log in
    log_in_button = driver.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button') 
    log_in_button.click()

def SwitchIP():
    os.system("protonvpn-cli status")
    os.system("protonvpn-cli c --tor")
    os.system("protonvpn-cli status")

def Restart():
    driver.close()
    SwitchIP()
    driver = Driver()
    Login()


def Keywords():
    keys = []
    while True:
        keyword = input('\nIntroduce keyword to search. Press enter to continue: ')
        if len(keyword) < 1:
            if len(keys) == 0: print('You must introduce at least one keyword...')
            else: 
                print('\nYour keywords are: '); 
                print(*keys, sep=', ')
                break
        else: keys.append(keyword)
    return keys

def GoogleSearch( keywords ):
    # go to google
    driver.get("https://www.google.com")
    # cookies acceptance
    try:
        cookies_button = driver.find_element(by=By.ID, value='L2AGLb') 
        cookies_button.click()
    except:pass
    # select google input
    search_query = driver.find_element(by=By.NAME, value='q')
    # make search string
    search = 'site:linkedin.com/in/'
    for key in keywords:
        search = search + ' AND ' + '"'+key+'"'
    print('\nYou are searching... ', search)
    # introduce search
    search_query.send_keys(search)
    search_query.send_keys(Keys.RETURN)


def GetLinks( db, pages ):
    urls = []; linkedins = []
    while pages > 1:
        try:
            linkedins = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
        except:
            input('To continue press enter... ')
        for i in range(len(linkedins)):
            #sleep(random.randint(1,3))
            url = linkedins[i].find_element(by=By.CSS_SELECTOR, value='a').get_attribute('href')
            if 'linkedin' in url:
                urls.append(url)
        print(len(db)+len(urls))
        pages -= 1
        try:
            next_button = driver.find_element(By.ID, 'pnnext') 
            next_button.click()
        except: 
            cont = input('Press enter to continue scrapping... ')
            if len(cont) < 1: continue 
            else: break
    return urls

def GetData():
    db = []
    while True:
        try:
            GoogleSearch(Keywords())
            urls = GetLinks(db, 100)
            db = db + urls
        except:
            input('To continue press enter... ')
        ans = input('You found '+str(len(db))+' urls. Would you like to add other keywords to expand your db? y(yes) or n(no): ')
        if len(ans) < 1 or ans == 'y' or ans == 'Y' or ans == 'yes' or ans == 'YES':
            continue
        else: break
    db = list(set(db))
    return db

Login()

Data = GetData()

name = input('Insert name of the database? ')
input('Press enter to confirm... ')
np.savetxt(name+'.csv', Data, delimiter =", ", fmt ='% s')

driver.close()


