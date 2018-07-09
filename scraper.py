#! /usr/bin/env python

import requests
import os
import re
from selenium import webdriver
from dotenv import load_dotenv
from pathlib import Path
from time import sleep
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

QUERY_INTERVAL = 10 # minutes

gym_url = 'https://www.puregym.com/members/'
login_url = 'https://www.puregym.com/Login/?ReturnUrl=%2Fmembers%2F'
login_payload = {
    "email": str(os.getenv("puregym_email")),
    "pin": str(os.getenv("puregym_pin")),
}

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841')
options.add_argument('headless')

def fetch_activity():
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(login_url)

    # Log in
    driver.find_element_by_id('email').send_keys(login_payload['email'])
    driver.find_element_by_id('pin').send_keys(login_payload['pin'])
    driver.find_element_by_id('login-submit').click()
    sleep(2)

    # Parse out number of people at the gym
    span = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[1]/div/p[1]/span')
    num_people = re.search(r'\d+', span.text).group()

    driver.stop_client()
    driver.quit()

    return num_people

if __name__ == '__main__':
    print('PureGym web scraper...')
    while True:
        num_people = fetch_activity()
        # TODO get current date and time Tue 10 Jul 00:57:50 2018
        # Push number of people and date and time to a csv

        print(num_people)
        print('waiting {} minutes'.format(QUERY_INTERVAL))
        sleep(QUERY_INTERVAL * 60)
