import scrapy

class QuotesScrapyItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
