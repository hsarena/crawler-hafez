# -*- coding: utf-8 -*-
import scrapy
from hafez.items import HafezItem


class FaalSpider(scrapy.Spider):
    name = 'faal'
    allowed_domains = ['www.seyedrezabazyar.com']

    faals = list(range(1, 495))
    start_urls = ['https://www.seyedrezabazyar.com/hafez/poetry-{0}'.format(faal) for faal in faals]

    custom_settings = {
        'DEPTH_LIMIT': '1',
    }

    def parse(self, response):
        faal = []
        rows = response.xpath('//*[@id="the-post"]/div/div[1]/div[1]/div')
        for row in rows:
            line = '____'.join(row.xpath('div/p/text()').getall())
            print("LINE             : ",line)
            faal.append(line)

        faal = '/n'.join(faal)
        print(faal)

        item = HafezItem()
        item['title'] = response.xpath('//*[@id="the-post"]/div/div[1]/div[1]/h4/text()').get()
        item['voice'] = response.xpath('//*[@id="the-post"]/div/div[1]/figure/audio/@src').get()
        item['faal'] = faal
        print(item)
        return item
