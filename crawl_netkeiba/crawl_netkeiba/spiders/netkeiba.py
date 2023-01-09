import scrapy


class NetkeibaSpider(scrapy.Spider):
    name = 'netkeiba'
    allowed_domains = ['db.netkeiba.com']
    start_urls = ['http://db.netkeiba.com/']

    def parse(self, response):
        pass
