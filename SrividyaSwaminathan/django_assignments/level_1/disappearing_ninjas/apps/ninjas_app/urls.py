
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.show),
    url(r'^ninjas/(?P<ninjas_color>[a-z]+)$', views.ninjas)
]
