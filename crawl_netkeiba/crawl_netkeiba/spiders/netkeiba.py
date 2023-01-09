import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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
        check_date = driver.find_element(By.XPATH, '//select[@name="start_year"]')
        select_2017 = Select(check_date)
        select_2017.select_by_value('2017')
        sleep(1)
        for i in range(5, 10):
            check_place = driver.find_element(By.XPATH, f'//input[@id="check_Jyo_0{i}"]')
            check_place.click()
        sleep(1)
        X = driver.find_element(By.XPATH, '//img[@id="gn_interstitial_close_icon"]')
        X.click()
        sleep(1)
        for i in range(1600, 2700, 100):
            check_distance = driver.find_element(By.XPATH, f'//input[@id="check_kyori_{i}"]')
            check_distance.click()
        check_distance_3000 = driver.find_element(By.XPATH, '//input[@id="check_kyori_3000"]')
        check_distance_3000.click()
        check_distance_3200 = driver.find_element(By.XPATH, '//input[@id="check_kyori_3200"]')
        check_distance_3200.click()
        sleep(1)
        check_display = driver.find_element(By.XPATH, '//select[@name="list"]')
        select_100 = Select(check_display)
        select_100.select_by_value('100')
        sleep(1)
        search = driver.find_element(By.XPATH, '//input[@value="検索"]')
        search.click()
        sleep(1)

        driver.save_screenshot('test.png')
