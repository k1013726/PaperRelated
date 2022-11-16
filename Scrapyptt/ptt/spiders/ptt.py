# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:05:17 2022

@author: k1013
"""

from ptt.items import PostItem
import scrapy
import time

class PTTSpider(scrapy.Spider):
    #爬蟲命名
    name = 'ptt'
    
    #允許的網域，可以允許多個網域
    allowed_domains = ['ptt.cc']
    
    #起始網址，可以允許多個網域  
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index39154.html']
    
    #自動判別是否18歲
    def parse(self, response):
        for i in range(1000):
            time.sleep(1)
            url = "https://www.ptt.cc/bbs/Gossiping/index" + str(39154 - i) + ".html"
            yield scrapy.Request (url,callback=self.parseArticle)
   
    def parseArticle(self, response):
        item = PostItem()
        target = response.css("div.r-ent")
    
    
        for tag in target:
            try:
                item['title'] = tag.css("div.title a::text")[0].extract()
                item['author'] = tag.css('div.author::text')[0].extract()
                item['date'] = tag.css('div.date::text')[0].extract()
                item['push'] = tag.css('span::text')[0].extract()
                item['url'] = tag.css('div.title a::attr(href)')[0].extract()
    
                yield item
    
            except IndexError:
                pass
            continue