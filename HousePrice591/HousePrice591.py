# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:50:54 2022

@author: admin
"""

import scrapy
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


start_urls = 'https://market.591.com.tw/5859630'


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
time.sleep(1)
resp = requests.get(start_urls,headers=headers)

soup = BeautifulSoup(resp.text,'html5lib')

title = soup.title

text=soup.findAll('address')

print(text)