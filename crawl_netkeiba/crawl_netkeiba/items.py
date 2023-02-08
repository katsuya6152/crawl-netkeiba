# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlNetkeibaItem(scrapy.Item):
    id = scrapy.Field()
    race_name = scrapy.Field()
    race_place = scrapy.Field()
    number_of_entries = scrapy.Field()
    race_state = scrapy.Field()
    date = scrapy.Field()
