import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from time import sleep


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
        check_track = driver.find_element(By.XPATH, '//input[@id="check_track_1"]')
        check_track.click()
        sleep(1)
        check_track = driver.find_element(By.XPATH, '//input[@id="check_track_1"]')

        driver.save_screenshot('test.png')
