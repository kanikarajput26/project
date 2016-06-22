import xmltodict
import requests
from . import models


def wegGetter(url):
    g1 = requests.get(url)
    f1 = xmltodict.parse(g1.content)
    return f1

def processor1(content1):
    item1 = content1['rss']
    return item1

def processor2(content2):
    item2 = content2['channel']
    return item2

def processor3(content3):
    item3 = content3['item']
    return item3

def saver(item):
    _category = item['category']
    category = _category[0]
    _url = item['post-thumbnail']
    image_url = _url['url']
    _content = models.Content(cid="2",title=item['title'],category=category,description=item['description'],image_url=image_url,url=item['link'])
    _content.save()
    return