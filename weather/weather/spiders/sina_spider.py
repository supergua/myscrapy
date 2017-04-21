import os
import scrapy
from ..items import WeatherItem

class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["weather.sina.com.cn"]
    start_urls = ["http://weather.sina.com.cn/"]
    def parse(self, response):
        # filename = response.url.split('/')[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        items = []
        city = response.xpath('//h4[@id="slider_ct_name"]/text()').extract()
        #city2 = response.css('').text()
        for sel in response.xpath('//div[@class="blk_fc_c0_i"]'):
            item = WeatherItem()
            date = sel.xpath('p[1]/text()').extract()
            dayDesc1 = sel.xpath('p[3]/img[1]/@title').extract()
            dayDesc2 = sel.xpath('p[3]/img[2]/@title').extract()
            dayTemp = sel.xpath('p[5]/text()').extract()
           # print(date, dayDesc, dayTemp)
            item['date'] = date[0]
            item['dayDesc1'] = dayDesc1[0]
            item['dayDesc2'] = dayDesc2[0]
            item['dayTemp'] = dayTemp[0]
            items.append(item)
            print(item)
        return items