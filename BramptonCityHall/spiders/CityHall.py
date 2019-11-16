# -*- coding: utf-8 -*-
import scrapy
from ..items import BramptoncityhallItem

class CityhallSpider(scrapy.Spider):
    name = 'CityHall'   
    start_urls = [
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Jeff-Bowman/Pages/Contact-Us.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Gurpreet-Dhillon/Pages/Contact%20Form.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Pat-Fortini/Pages/Contact%20Form.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Michael-Palleschi/Pages/Contact%20Form.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Rowena-Santos/Pages/Contact-Us.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Harkirat-Singh/Pages/Contact-Us.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Paul-Vicente/Pages/Contact-Us.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Doug-Whillans/Pages/Contact-Form.aspx',
        'http://www.brampton.ca/EN/City-Hall/CouncilOffice/Charmaine-Williams/Pages/Contact-Us.aspx'
    ]

    def parse(self, response):
        item = BramptoncityhallItem()

        name = response.css('#ctl00_PlaceHolderMain_ctl02__ControlWrapper_RichHtmlField strong::text').extract_first()
        if name:
            yield name
        else:
            name = response.css('#ctl00_PlaceHolderMain_ctl02__ControlWrapper_RichHtmlField b::text').extract_first()
        if name != name:
            yield 'N/A'
        
        title = response.css('#pageTitle::text').extract_first()
        email = response.css('#ctl00_PlaceHolderMain_ctl02__ControlWrapper_RichHtmlField a::text').extract_first()

        item['name'] = name
        item['title'] = title
        item['email'] = email


        yield item
