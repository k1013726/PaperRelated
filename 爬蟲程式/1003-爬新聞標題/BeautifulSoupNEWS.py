# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 17:54:00 2022

@author: admin
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
# from selenium import webdriver
# import time

url ='https://www.mirrormedia.mg/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

resp = requests.get(url,headers=headers)



soup = BeautifulSoup(resp.text,'html5lib')


title = soup.title
sa=[]
for i in soup.findAll('h1'):
  h=i.find('span')
  if str(h)!='None':
      sa.append(h.string)
      

df = pd.DataFrame(sa, columns =["adess"]) 
df.to_csv('test.csv')
