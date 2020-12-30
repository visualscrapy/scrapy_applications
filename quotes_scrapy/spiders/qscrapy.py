import scrapy
from ..items import QuotesScrapyItem

class QscrapySpider(scrapy.Spider):
    name = 'qscrapy'
    def __init__(self, page_num='', **kwargs):
        self.start_urls = [f'http://quotes.toscrape.com/page/{page_num}']
        super().__init__(**kwargs)
        self.page_num = page_num

    custom_settings = {"FEEDS": {"output.csv": {"format": "csv"}, }, }

    def parse(self, response):
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            item = QuotesScrapyItem(
                title = quotes.css("span.text::text").extract_first(),
                author = quotes.css(".author::text").extract_first(),
                tags = quotes.css(".tag::text").extract_first()
            )
            yield item
            # yield from response.follow_all(css='ul.pager a', callback=self.parse)