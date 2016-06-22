import requests
import simplejson
from . import models

def wegGetter(url):
	f1 = requests.get(url)
	g1 = simplejson.loads(f1.content)
	return g1

def processor(content):
	items = content['rss']['channel']['item']
	return items

def saver(item):
	_content = models.Content(cid="12",title=item['title'],url=item['link'],image_url=item['media:content']['@attributes']['url'],category=item['category'],description=item['description'])
	_content.save()
	return

# def main():
# 	g1 = wegGetter("http://www.indiatimes.com/feeds/feeds.json")
# 	items = processor(g1)
# 	for item in items:
# 		saver(item)
# 	return


