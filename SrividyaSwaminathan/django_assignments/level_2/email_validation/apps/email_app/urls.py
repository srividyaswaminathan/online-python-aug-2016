from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_email$', views.process_email),
    url(r'^show_email$', views.show_email),
    url(r'^delete/(?P<id>\d+)$', views.destroy)
]
