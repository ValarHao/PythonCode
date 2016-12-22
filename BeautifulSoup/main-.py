from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html)
names = bs.findAll("span", {"class": "green"})
for name in names:
    print(name.get_text())
