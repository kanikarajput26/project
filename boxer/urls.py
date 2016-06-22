from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'applet/list/$',views.getApplets,name="listapplets"),
    url(r'applet/content/',views.getContent,name="content"),
    url(r'applet/content_filter/',views.getFilter,name="filter"),

]