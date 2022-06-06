# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter
import pymongo
from .items import RentalscraperItem

from dotenv import load_dotenv
load_dotenv()


class RentalscraperPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    collection_name = os.getenv('COLLECTION_NAME')

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB', os.getenv('DB_NAME'))
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri, ssl=True)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # print('URL--------->', item['url'])
        if self.db[self.collection_name].count_documents({'url': item['url']}, limit=1) == 0:
            self.db[self.collection_name].insert_one(item)
        else:
            return f'Document, {item} already exists'
        return item
