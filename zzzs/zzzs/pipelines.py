# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ZzzsPipeline(object):
    def __init__(self):
        self.f=open("a.txt","w+",encoding="utf-8")

    def process_item(self, item, spider):
        msg=json.dumps(dict(item),ensure_ascii=False)
        self.f.write(msg+"\n")
        return item