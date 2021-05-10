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

# Config
SLEEP_TIME = 2
NUM_OF_SCROLL = 7

main_url = 'https://m.facebook.com/MSBVietNam/'

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get(main_url)

# Log in
login_url = 'https://m.facebook.com/login.php?next=' + main_url
driver.get(login_url)
login_email_input = driver.find_element_by_id('m_login_email')
login_email_input.send_keys('')
login_pwd_input = driver.find_element_by_id('m_login_password')
login_pwd_input.send_keys('')
login_pwd_input.send_keys(Keys.ENTER)
sleep(SLEEP_TIME)

"""
driver.get('https://m.facebook.com/checkpoint/?next=' + main_url)
approvals_code_input = driver.find_element_by_id('approvals_code')
approvals_code_input.send_keys(input())
approvals_code_input.send_keys(Keys.ENTER)
driver.find_element_by_id('checkpointSubmitButton').click()
"""

# Traverse all stories
driver.maximize_window()
for i in range(NUM_OF_SCROLL):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(SLEEP_TIME)
story_feedbacks = driver.find_elements_by_xpath('//div[@class="story_body_container"]/following-sibling::footer//a')

# Go into a post
story_url = story_feedbacks[0].get_attribute('href')
driver.get(story_url)
sleep(SLEEP_TIME)
print('Successfully go into a post')

# Go into reaction page
reaction_url = driver.find_element_by_xpath('//div[@id="add_comment_switcher_placeholder"]/following-sibling::div//a').get_attribute('href')
driver.get(reaction_url)
sleep(SLEEP_TIME)
print('Successfully go into reaction page')

# Go into profile
profile_url = driver.find_element_by_xpath('//div[@id="root"]//a').get_attribute('href')
driver.get(profile_url)
sleep(SLEEP_TIME)
print('Successfully go into profile')

# Go into details
details_url = driver.find_element_by_xpath('//div[@id="profile_intro_card"]//a').get_attribute('href')
driver.get(details_url)
sleep(SLEEP_TIME)
print('Successfully go into details')

# About me
about_me_xpath = '//div[@class="timeline aboutme"]'

work_spans = driver.find_elements_by_xpath(about_me_xpath + '//div[@id="work"]//span')
if len(work_spans) > 0:
    print('Work: ' + work_spans[0].get_attribute('textContent'))
    
living_h4s = driver.find_elements_by_xpath(about_me_xpath + '//div[@id="living"]//h4')
for i in range(1, len(living_h4s), 2):
    print(living_h4s[i].get_attribute('textContent') + ": " + living_h4s[i-1].get_attribute('textContent'))

relationship_divs = driver.find_elements_by_xpath(about_me_xpath + '//div[@id="relationship"]//div')
for relationship_div in relationship_divs:
    relationship_text = relationship_div.get_attribute('textContent')
    if relationship_text != '' and relationship_text != 'Mối quan hệ':
        print('Relationship: ' + relationship_text)
        break