# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    name = scrapy.Field()
    screen = scrapy.Field()
    cpu = scrapy.Field()
    ram = scrapy.Field()
    rom = scrapy.Field()
    camera = scrapy.Field()
    selfie = scrapy.Field()
    pin = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()

class DetailItem(scrapy.Item):
    name = scrapy.Field()
    
