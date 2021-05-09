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
story_url = story_feedbacks[0].get_attribute('href')
driver.get(story_url)
sleep(1)
print('Successfully go into a post')

# Go into reaction page
reaction_url = driver.find_element_by_xpath('//div[@id="add_comment_switcher_placeholder"]/following-sibling::div//a').get_attribute('href')
driver.get(reaction_url)
sleep(1)
print('Successfully go into reaction page')

# Go into profile
profile_url = driver.find_element_by_xpath('//div[@id="reaction_profile_browser"]//a').get_attribute('href')
driver.get(profile_url)
sleep(1)
print('Successfully go into profile')

# Go into details
details_url = driver.find_element_by_xpath('//div[@id="profile_intro_card"]//a').get_attribute('href')
driver.get(details_url)
sleep(1)
print('Successfully go into details')

# About me
about_me = driver.find_element_by_xpath('//div[@class="aboutme"]')
print(about_me.get_attribute('innerHTML'))