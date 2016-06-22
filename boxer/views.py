from django.http import HttpResponse
from . import models
import simplejson

def getApplets(request):
    applets = models.Applets.objects.all()
    newlist = []
    for a in applets:
        newlist.append(a.to_json())
    return HttpResponse(simplejson.dumps(newlist),content_type="application/json")


def getContent(request):
    start=0
    end=10
    id = request.GET['id']
    content = models.Content.objects(cid = id).all()[start:end]
    contentlist = []
    for c in content:
        contentlist.append({"title":c.title,"cid":c.cid,"description":c.description,"url":c.url,"image_url":c.image_url,"category":c.category})
    return HttpResponse(simplejson.dumps(contentlist),content_type="application/json")

def getFilter(request):
    start=0
    end=10
    _Filter= request.GET['filter']
    id = request.GET['id']
    content = models.Filters.objects(_filter =_Filter,cid=id).all()[start:end]
    filteredlist = []
    for f in content:
        filteredlist.append(f.to_json())
    return HttpResponse(simplejson.dumps(filteredlist),content_type="application/json")


