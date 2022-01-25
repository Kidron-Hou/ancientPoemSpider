#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : verse_spider.py
# @Description:
# @Time       : 2021-12-28 下午 9:23
# @Author     : Hou


import time
import scrapy
from datetime import datetime
from ancientPoemSpider.items import AncientpoemspiderItem


class VerseSpider(scrapy.Spider):
    name = 'poem'
    start_urls = 'https://so.gushiwen.cn/mingjus/default.aspx?page={p}&tstr=&astr=&cstr=&xstr='

    def start_requests(self):
        for i in range(5):
            url = self.start_urls.format(p=(i+1))
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        verse_list = response.xpath('//div[@class="left"]/div[@class="sons"]/div')
        for div in verse_list:
            item = AncientpoemspiderItem()
            item['verse'] = div.xpath('.//a[1]/text()').extract()[0]
            resource = div.xpath('.//a[2]/text()').extract()
            item['resource'] = resource[0] if resource else None
            item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            yield item
