# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZzzsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gaoxiao=scrapy.Field()      #报考高校
    name=scrapy.Field()         #姓名
    sex=scrapy.Field()          #性别
    middleSchool=scrapy.Field()        #就读中学
    province=scrapy.Field()         #省份