from django.conf.urls import include, url
from . import views

app_name='goodslist'
urlpatterns = [
    url(r'^list/$', views.list, name='list'),
  
]
 # url(r'^list/$',views.list,name='list'),