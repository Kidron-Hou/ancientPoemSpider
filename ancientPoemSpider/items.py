# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AncientpoemspiderItem(scrapy.Item):
    # define the fields for your item here like:
    verse = scrapy.Field()  # 诗句
    resource = scrapy.Field()  # 出处
    crawl_time = scrapy.Field()  # 抓取时间


    pass
