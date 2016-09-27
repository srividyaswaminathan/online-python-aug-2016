from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^products$', views.index, name="index" ),   #get
    url(r'^products/new$', views.new, name="new" ),
    url(r'^products$', views.create, name="create" ),  #post
    url(r'^products/(?P<id>\d+)$', views.show, name="show" ),
    url(r'^products/(?P<id>\d+)/edit$', views.edit, name="edit" ),
    url(r'^products/(?P<id>\d+)/update$', views.update, name="update" ),  #put or patch
    url(r'^products/(?P<id>\d+)/destroy$', views.destroy, name="destroy" ), #delete 
]
	