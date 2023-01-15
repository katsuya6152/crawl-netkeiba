import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
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
        # check_display = driver.find_element(By.XPATH, '//select[@name="list"]')
        # select_100 = Select(check_display)
        # select_100.select_by_value('100')
        # sleep(1)
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
            results = []
            last_rank = 0
            for index, tr in enumerate(tr_elements):
                if index == 0:
                    continue
                
                result = {
                    'Rank': tr.xpath('./td[position()=1]/text()').get(),
                    'Box': tr.xpath('./td[position()=2]/span/text()').get(),
                    'Horse order': tr.xpath('./td[position()=3]/text()').get(),
                    'Horse name': tr.xpath('./td[position()=4]/a/text()').get(),
                    'Sex and age': tr.xpath('./td[position()=5]/text()').get(),
                    'Burden weight': tr.xpath('./td[position()=6]/text()').get(),
                    'Jockey': tr.xpath('./td[position()=7]/a/text()').get(),
                    'Time': tr.xpath('./td[position()=8]/text()').get(),
                    'Difference': tr.xpath('./td[position()=9]/text()').get(),
                    'Transit': tr.xpath('./td[position()=11]/text()').get(),
                    'Climb': tr.xpath('./td[position()=12]/span/text()').get(),
                    'Odds': tr.xpath('./td[position()=13]/text()').get(),
                    'Popularity': tr.xpath('./td[position()=14]/span/text()').get(),
                    'Horse weight': tr.xpath('./td[position()=15]/text()').get(),
                    'Horse trainer': tr.xpath('./td[position()=19]/a/text()').get(),
                    'Horse owner': tr.xpath('./td[position()=20]/a/text()').get(),
                    'Prize': tr.xpath('./td[position()=21]/text()').get(),
                }
                results.append(result)
                last_rank = index
            yield {
                'Race Name': sel.xpath('//dd/h1/text()').get(),
                'Race State': sel.xpath('//diary_snap_cut/span/text()').get(),
                'Date': sel.xpath('//div[@class="data_intro"]/p/text()').get(),
                'Race place': sel.xpath('//div[@class="race_head_inner"]/ul/li/a[@class="active"]/text()').get(),
                'Number of Entries': last_rank,
                'Result': results
            }