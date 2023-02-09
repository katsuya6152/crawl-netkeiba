# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .database import session, Base
from .race import Race, RaceResult


class GetRacePipeline:
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


class GetRaceResultPipeline:
    def process_item(self, item, spider):
        horse_id_exists = session.query(RaceResult).filter(RaceResult.horse_id==item['horse_id']).first()
        if(horse_id_exists == None):
            race_result = RaceResult()
            race_result.id = item['id']
            race_result.horse_id = item['horse_id']
            race_result.rank = item['rank']
            race_result.box = item['box']
            race_result.horse_order = item['horse_order']
            race_result.horse_name = item['horse_name']
            race_result.sex_and_age = item['sex_and_age']
            race_result.burden_weight = item['burden_weight']
            race_result.jockey = item['jockey']
            race_result.time = item['time']
            race_result.difference = item['difference']
            race_result.transit = item['transit']
            race_result.climb = item['climb']
            race_result.odds = item['odds']
            race_result.popularity = item['popularity']
            race_result.horse_weight = item['horse_weight']
            race_result.horse_trainer = item['horse_trainer']
            race_result.horse_owner = item['horse_owner']
            race_result.prize = item['prize']
            session.add(race_result)
            session.commit()
        return item
