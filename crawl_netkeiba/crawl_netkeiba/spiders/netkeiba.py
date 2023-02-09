import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from crawl_netkeiba.items import CrawlNetkeibaItem, CrawlRaceResultItem


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

        race_url_elements = driver.find_elements(By.XPATH, '//tr[position()>1]//td[position()=5]/a')
        urls = [i.get_attribute('href') for i in race_url_elements]
        for url in urls:
            driver.get(url)
            html = driver.page_source
            sel = Selector(text=html)
            tr_elements = sel.xpath('//table[@class="race_table_01 nk_tb_common"]/tbody/tr')
            id = sel.xpath('substring(//ul[@class="race_place fc"]/li/a[@class="active"]/@href, 7, 12)').get()
            yield CrawlNetkeibaItem(
                id = id, 
                race_name = sel.xpath('//dd/h1/text()').get(), 
                race_place = sel.xpath('//div[@class="race_head_inner"]/ul/li/a[@class="active"]/text()').get(), 
                number_of_entries = len(tr_elements), 
                race_state = sel.xpath('//diary_snap_cut/span/text()').get(), 
                date = sel.xpath('//div[@class="data_intro"]/p/text()').get()
            )

            for index, tr in enumerate(tr_elements):
                if index == 0:
                    continue

                yield CrawlRaceResultItem(
                    id = id,
                    horse_id = id + str(index).zfill(2),
                    rank = tr.xpath('./td[position()=1]/text()').get(),
                    box = tr.xpath('./td[position()=2]/span/text()').get(),
                    horse_order = tr.xpath('./td[position()=3]/text()').get(),
                    horse_name = tr.xpath('./td[position()=4]/a/text()').get(),
                    sex_and_age = tr.xpath('./td[position()=5]/text()').get(),
                    burden_weight = tr.xpath('./td[position()=6]/text()').get(),
                    jockey = tr.xpath('./td[position()=7]/a/text()').get(),
                    time = tr.xpath('./td[position()=8]/text()').get(),
                    difference = tr.xpath('./td[position()=9]/text()').get(),
                    transit = tr.xpath('./td[position()=11]/text()').get(),
                    climb = tr.xpath('./td[position()=12]/span/text()').get(),
                    odds = tr.xpath('./td[position()=13]/text()').get(),
                    popularity = tr.xpath('./td[position()=14]/span/text()').get(),
                    horse_weight = tr.xpath('./td[position()=15]/text()').get(),
                    horse_trainer = tr.xpath('./td[position()=19]/a/text()').get(),
                    horse_owner = tr.xpath('./td[position()=20]/a/text()').get(),
                    prize = tr.xpath('./td[position()=21]/text()').get()
                )