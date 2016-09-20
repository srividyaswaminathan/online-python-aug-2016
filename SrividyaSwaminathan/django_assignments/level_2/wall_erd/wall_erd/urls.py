from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('apps.wall_app.urls')),
]
