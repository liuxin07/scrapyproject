# -*- coding: utf-8 -*-
import scrapy

class GithubSpider(scrapy.Spider):
    name = 'github'

    @property
    def start_usrls(self):
        return (['https://github.com/shiyanlou?tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoyMToxNlrOBZKV2w%3D%3D&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNS0wMS0yNlQwODoxNzo1M1rOAcd_9A%3D%3D&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNS0wMS0yNlQwODoxNzo1M1rOAcd_9A%3D%3D&tab=repositories'])
    def parse(self, response):
        for rep in response.css('li.public'):
            item = DataItem({
            'name':rep.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
            'update_time':rep.xpath('.//relative-time/@datetime').extract_first()
            }) 
            yield item
