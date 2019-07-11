from django.conf.urls import url
from . import views

urlpatterns = [
    # localhost:8000{/}
    url(r"^$", views.index),
    # localhost:8000/other
    url(r"^other$", views.other),
    # localhost:8000/user/1
    # localhost:8000/user/2
    # localhost:8000/user/<user_id>
    url(r"^user/(?P<user_id>\d+)$", views.show),
]