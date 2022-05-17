#!/usr/bin/python

from csv import reader
import time
import random
from bs4 import BeautifulSoup as bs
import pandas as pd
from login import driver
from login import Login

name = input('\nInsert name of the database... ')
db = open(name+'.csv')
db = list(reader(db))

Login()

def scroll( sleep ):
    start = time.time()
    initialScroll = 0
    finalScroll = 1000
    while True:
        driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
        initialScroll = finalScroll
        finalScroll += 1000
        time.sleep(3)
        end = time.time()
        if round(end - start) > sleep:
            break
          

def GetData( url ):

    driver.get(url)
    print(url+'...')

    ranint = random.randint(10,25)
    print('Sleeping '+str(ranint)+' seconds...')
    scroll( ranint )

    html = driver.page_source
    soup = bs(html)

    name = ''
    try:
        name = soup.find('h1').get_text()
        #print(name)
    except: pass

    title = ''
    try:
        title = soup.find('div', class_='text-body-medium break-words').get_text()
        title = title.replace('\n      ', '')
        title = title.replace('\n    ', '')
        #print(title)
    except: pass

    company = ''
    try:
        company = soup.find('h2', class_='pv-text-details__right-panel-item-text hoverable-link-text break-words text-body-small inline').get_text()
        company = company.replace('\n\n\n    ', '')
        company = company.replace('\n  \n\n', '')
        #print(company)
    except: pass

    location = ''
    try:
        location = soup.find('span', class_='text-body-small inline t-black--light break-words').get_text()
        location = location.replace('\n      ', '')
        location = location.replace('\n    ', '')
        #print(location)
    except: pass

    about = ''
    try:
        about = soup.find('div', class_='pv-shared-text-with-see-more t-14 t-normal t-black display-flex align-items-center').find('span').get_text()
        #print(about)
    except: pass

    followers = 0
    try:
        followers = soup.find('p', class_='pvs-header__subtitle text-body-small').find('span').get_text()
        followers = int(followers.replace(' followers', ''))
        #print(followers)
    except: pass

    df = {  'name': name,
            'title': title,
            'comapny': company,
            'location': location,
            'about': about,
            'followers': followers,
            'url': url
         }

    return df

df = pd.DataFrame(columns=['name','title','company','location','about','followers','url'])

for profile in db:
    df = df.append(GetData(profile[0]), ignore_index=True)
    print(df)
