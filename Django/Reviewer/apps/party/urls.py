from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/create$', views.create_user),
    url(r'^party/create$', views.create_party),
]