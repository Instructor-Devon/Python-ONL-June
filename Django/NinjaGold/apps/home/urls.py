from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^playername$', views.player),
    url(r'^getgold$', views.gold),
    url(r'^death$', views.death),
    
]