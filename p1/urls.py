#imports
from django.conf.urls import patterns,url
from p1 import views
#url dispatcher
urlpatterns= patterns('',url(r'^$',views.index,name="index"))
