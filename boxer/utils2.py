import requests
import simplejson
from . import models

def wegGetter(url):
    f1 = requests.get(url)
    g1 = simplejson.loads(f1.content)
    return g1

def processor(content):
    items = content['channel']
    return items

def saver(item):
    a_split = item['description'].split(';')
    a_list = {'image_url':';'.join(a_split[:6]),'description':';'.join(a_split[6:])}
    _content = models.Content(cid="1",title=item['title'],image_url=a_list['image_url'],category=item['category'],url=item['link'],description=a_list['description'])
    _content.save()
    return

