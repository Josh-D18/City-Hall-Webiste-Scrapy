# -*- coding: utf-8 -*-
import scrapy
from ..items import BramptoncityhallItem, BramptoncityhallMayorItem

class CityhallSpiderMayor(scrapy.Spider):
    name = 'CityHallMayor'   
    start_urls = [
        'http://www.brampton.ca/EN/City-Hall/Mayor-Office/Pages/Contact-Us.aspx',
    ]

    def parse(self, response):
        item = BramptoncityhallMayorItem()

        position = response.css('.col-sm-6:nth-child(1) p::text').extract_first()    
        title = response.css('#pageTitle::text').extract_first()
        phone_number = response.css('.col-sm-6+ .col-sm-6 p::text').extract_first()
        if phone_number:
            yield phone_number
        else:
            yield 'Please Use My Email Address To Contact Me'

        item['position'] = position
        item['title'] = title
        item['phone_number'] = phone_number

        yield item
