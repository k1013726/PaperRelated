# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:47:43 2022

@author: k1013
"""


from  HousePriceScrapy.items import HousepricescrapyItem
import scrapy
import time
from bs4 import BeautifulSoup
import requests
class HousepriceSpider(scrapy.Spider):
    #爬蟲命名
    name = 'Houseprice'
    
    #允許的網域，可以允許多個網域
    allowed_domains = ['market.591.com.tw']
    
    #起始網址，可以允許多個網域  
    start_urls = 'https://market.591.com.tw/5859630'
   
    def parse(self, response):
        item = HousepricescrapyItem()
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        time.sleep(1)
        start_urls = "https://www.mirrormedia.mg/"
        resp = requests.get(start_urls,headers=headers)



        soup = BeautifulSoup(resp.text,'html5lib')
        
        
        title = soup.title
        print(title)
        #=[]
        # for i in soup.findAll('h1'):
        #   h=i.find('span')
        #   if str(h)!='None':
        #       print(h.string)
        #       item['DealDate']=h.string
        #       yield item
    
