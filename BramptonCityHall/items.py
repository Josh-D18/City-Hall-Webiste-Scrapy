# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BramptoncityhallItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    name = scrapy.Field()
    email = scrapy.Field()



class BramptoncityhallMayorItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    position = scrapy.Field()
    phone_number = scrapy.Field()