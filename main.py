from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime


def getLinks(articleUrl):
    html = urlopen(f'http://en.wikipedia.org{articleUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a',
                                                          href=re.compile('^(/wiki/)((?!:).)*$'))


random.seed(datetime.datetime.now())
links = getLinks('/wiki/Kevin_Bacon')
# print(links[random.randint(0, len(links)-1)].attrs['href'])
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
