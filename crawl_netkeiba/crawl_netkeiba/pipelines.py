# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .database import session, Base
from .race import Race


class CrawlNetkeibaPipeline:
    def process_item(self, item, spider):
        races = Race()
        races.race_name = item['race_name']
        races.race_place = item['race_place']
        races.number_of_entries = item['number_of_entries']
        races.race_state = item['race_state']
        races.date = item['date']

        session.add(races)
        session.commit()

        return item
