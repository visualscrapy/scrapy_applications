import scrapy

class Page(scrapy.Item):
    # url = scrapy.Field()
    # size = scrapy.Field()
    # status = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
