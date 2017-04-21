# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import scrapy.exceptions

class WeatherPipeline(object):
    word_to_filter = ["过滤词"]

    def __init__(self):
        self.file = codecs.open('weather_data.json', 'wb', encoding='utf-8')
    def process_item(self, item, spider):
        for word in self.word_to_filter:
            if word==item['dayDesc1']:
                raise scrapy.exceptions.DropItem("Contains forbidden word: %s" % word)
        line = json.dumps(dict(item), ensure_ascii=False, indent=4) + '\n'
        self.file.write(line)
        return item