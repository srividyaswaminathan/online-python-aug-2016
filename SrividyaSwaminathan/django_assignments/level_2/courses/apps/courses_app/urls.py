from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index" ),
    url(r'^courses/add_course$', views.add_course, name="add_course"),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name="destroy")
]
