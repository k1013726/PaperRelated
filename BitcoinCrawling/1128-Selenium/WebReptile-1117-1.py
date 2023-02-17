# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import time


import os
if not os.path.isdir("Article"):os.mkdir("Article")

#from fake_useragent import UserAgent
driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.get('https://tts-nptu.funday.asia');

driver.find_element_by_id('email').send_keys('CBF107014')
driver.find_element_by_id('password').send_keys('CBF107014')



driver.find_element_by_class_name('sign_in_buttonjpg').click()
driver.get('https://tts-nptu.funday.asia/default/Lttc.asp');




txt='健身房'

   
time.sleep(1)
driver.find_element_by_xpath('//*[text()="'+txt+'"]').click()
time.sleep(1)

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="newsdiv"]/iframe'))
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="right"]/iframe'))
time.sleep(1)
  
driver.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[5]/td/a/img').click()
    
driver.close()
