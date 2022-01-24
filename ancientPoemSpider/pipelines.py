# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from sqlalchemy import create_engine


class AncientpoemspiderPipeline:

    def __init__(self):
        self.engine = create_engine('')

    def process_item(self, item, spider):

        return item
