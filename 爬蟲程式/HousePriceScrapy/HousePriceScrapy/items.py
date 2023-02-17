# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousepricescrapyItem(scrapy.Item):
    DealDate= scrapy.Field()
    HouseAddress= scrapy.Field()
    HouseType= scrapy.Field()
    TotalPrice= scrapy.Field()
    UnitPrice= scrapy.Field()
    
