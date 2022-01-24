#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : verse_spider.py
# @Description:
# @Time       : 2021-12-28 下午 9:23
# @Author     : Hou


import scrapy
from datetime import datetime
from ancientPoemSpider.items import AncientpoemspiderItem


class VerseSpider(scrapy.Spider):
    name = 'poem'
    start_urls = ['https://so.gushiwen.cn/mingjus/']

    def parse(self, response, **kwargs):
        verse_list = response.xpath('//div[@class="left"]/div[@class="sons"]/div')
        for div in verse_list:
            item = AncientpoemspiderItem()
            item['verse'] = div.xpath('.//a[1]/text()').extract()
            item['resource'] = div.xpath('.//a[2]/text()').extract()
            item['crawl_time'] = datetime.now()

            yield item
