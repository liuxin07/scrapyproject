# -*- coding: utf-8 -*-
import scrapy
from data.items import DataItem
class GithubSpider(scrapy.Spider):
    name = 'github'

    @property
    def start_urls(self):
        return ['https://github.com/shiyanlou?tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoyMToxNlrOBZKV2w%3D%3D&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNS0wMS0yNlQwODoxNzo1M1rOAcd_9A%3D%3D&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNS0wMS0yNlQwODoxNzo1M1rOAcd_9A%3D%3D&tab=repositories']

    def parse(self, response):
        for rep in response.css('li.public'):
            item = DataItem()
            item['name'] = rep.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)')
            item['update_time'] = rep.xpath('.//relative-time/@datetime').extract_first()
            data_url = response.urljoin(rep.xpath('.//h3/a/@href').extract_first())
            request = scrapy.Request(data_url, callback=self.parse_data)
            request.meta['item'] = item
            yield request

    def parse_data(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('.//li[1]//a/span/text()').re_first(r'\n\s*(.*)')
        item['branches'] = response.xpath('.//li[2]/a/span/text()').re_first(r'\n\s*(.*)')
        item['releases'] = response.xpath('.//li[3]/a/span/text()').re_first(r'\n\s*(.*)')
        yield item
