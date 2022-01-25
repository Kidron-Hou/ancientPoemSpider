# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ancientPoemSpider.domain import Poems

class AncientpoemspiderPipeline:

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/ancient_poem?charset=UTF8MB4')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


    def process_item(self, item, spider):
        poem = Poems()
        poem.poem_verse = item['verse']
        poem.poem_name = item['resource']
        poem.create_time = item['crawl_time']

        self.session.add(poem)
        self.session.commit()



