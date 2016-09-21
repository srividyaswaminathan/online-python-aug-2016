from django.conf.urls import url, include # Notice we added include
from . import views 
urlpatterns = [
      url(r'^', views.index) # And now we use include to pull in our first_app.urls...
  ]