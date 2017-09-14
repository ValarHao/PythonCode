# -*- coding: utf-8 -*-

import requests

from lxml import html

r = requests.get('https://movie.douban.com/top250')
tree = html.fromstring(r.text)
movies = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()')
print movies[0]
