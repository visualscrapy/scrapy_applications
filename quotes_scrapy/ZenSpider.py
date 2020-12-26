import scrapy
from items import Page
class ZenSpider(scrapy.Spider):
    def __init__(self):
        super().__init__()

    name = 'quotes'
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 2, "FEEDS": {"items.csv": {"format": "csv"}, }, }
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = []
        all_div_quotes = response.css("div.quote")

        for quotes in all_div_quotes:
            item = Page(
            title = quotes.css("span.text::text").extract_first(),
            author = quotes.css(".author::text").extract_first(),
            tag = quotes.css(".tag::text").extract_first()
            )
            yield item
            yield from response.follow_all(css='ul.pager a', callback=self.parse)