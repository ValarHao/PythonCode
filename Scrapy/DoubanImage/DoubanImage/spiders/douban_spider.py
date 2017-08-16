# -*- coding: utf-8 -*-

import scrapy
from DoubanImage.items import DoubanimageItem

class DoubanImageSpider(scrapy.Spider):
    name = 'douban_image'
    allowed_domains = ["https://movie.douban.com/"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanimageItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['image_urls'] = movie.xpath('.//div[@class="pic"]/a/img/@src').extract()
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield scrapy.Request(next_url, headers=self.headers)
