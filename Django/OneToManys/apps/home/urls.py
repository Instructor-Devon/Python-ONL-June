from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^players$', views.create_player),
    url(r'^players/(?P<player_id>\d+)$', views.player),
    url(r'^teams/(?P<team_id>\d+)$', views.team),
]