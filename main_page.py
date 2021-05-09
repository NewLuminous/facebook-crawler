# -*- coding: utf-8 -*-
"""
Created on Mon May 10 01:14:04 2021

@author: Admin
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(ChromeDriverManager().install())

main_url = 'https://m.facebook.com/MSBVietNam/'
#driver.get(main_url)

# Log in
login_url = 'https://m.facebook.com/login.php?next=' + main_url
driver.get(login_url)
login_email_input = driver.find_element_by_id('m_login_email')
login_email_input.send_keys('')
login_pwd_input = driver.find_element_by_id('m_login_password')
login_pwd_input.send_keys('')
login_pwd_input.send_keys(Keys.ENTER)

# Traverse all stories
driver.maximize_window()
for i in range(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
story_feedbacks = driver.find_elements_by_xpath('//div[@class="story_body_container"]/following-sibling::footer//a')

# Go into a post
story_url = story_feedbacks[2].get_attribute('href')
driver.get(story_url)