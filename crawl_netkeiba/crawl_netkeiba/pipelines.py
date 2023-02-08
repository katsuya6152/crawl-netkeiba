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
        id_exists = session.query(Race).filter(Race.id==item['id']).first()
        if(id_exists == None):
            race = Race()
            race.id = item['id']
            race.race_name = item['race_name']
            race.race_place = item['race_place']
            race.number_of_entries = item['number_of_entries']
            race.race_state = item['race_state']
            race.date = item['date']
            session.add(race)
            session.commit()
        return item
