# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:14:44 2022

@author: admin
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://market.591.com.tw/5859630/price")
time.sleep(1)

for i in range(15):
    driver.execute_script("var q=document.documentElement.scrollTop=0")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    


soup = BeautifulSoup(driver.page_source,'html5lib')
time.sleep(1)
driver.close()

# text=soup.find_all('address')

# for i in text:
#     print(i.string)

Haddess=[]
Hdetail=[]
for i in soup.findAll('address'):
    Haddess.append(i.string)
    
# for j in soup.findAll("p",class_="price"):
#     for i in j.findAll("span"):
#         #print(i)
#         Hdetail.append(j.string)

df = pd.DataFrame({"addess":Haddess})

df.to_csv('test.csv')