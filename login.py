# login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import credentials

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