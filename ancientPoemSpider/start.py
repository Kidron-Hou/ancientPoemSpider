#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : start.py
# @Description:
# @Time       : 2021-12-29 上午 7:33
# @Author     : Hou

from scrapy import cmdline

cmdline.execute('scrapy crawl poem'.split())