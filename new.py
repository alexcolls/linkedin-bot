
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.linkedin.com')

# login to a Linkedin account
def Login():
    # go to linkedin
    driver.get('https://www.linkedin.com')
    # select username input
    username = driver.find_element(by=By.CLASS_NAME, value='input__input')
    # email input
    email = input('Introduce a Linkedin email or press enter for default: ')
    if len(email) < 4:
        email = linkedin_email
    # write username input
    username.send_keys(email)
    # select password input
    password = driver.find_element(by=By.ID, value='session_password')
    # password input
    getpassword = getpass('Introduce password: ')
    if len(getpassword) < 4:
        getpassword = linkedin_pass
    # write password input
    password.send_keys(getpassword)
    # log in
    log_in_button = driver.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button') 
    log_in_button.click()

Login()