import scrapy
from scrapy_selenium import SeleniumRequest


class NetkeibaSpider(scrapy.Spider):
    name = 'netkeiba'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://db.netkeiba.com/?pid=race_search_detail',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        driver = response.meta['driver']
        driver.save_screenshot('test.png')
