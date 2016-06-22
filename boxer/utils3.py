import requests
import simplejson
import xmltodict
from . import models


def wegGetter(url):
    f1 = requests.get(url)
    g1 = xmltodict.parse(f1.content)
    return g1

def processor(content):
    items = content['rss']['channel']
    return items

def saver(item):
    title = item['title']
    category=item['category']
    description=item['description']
    image_url=item['post-thumbnail']
    url=item['link']
    _content = models.Content(cid="2",title=title,category=category,image_url=image_url,description=description,url=url)
    _content.save()
    return