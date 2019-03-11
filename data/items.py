import scrapy


class DataItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    update_time = scrapy.Field()
