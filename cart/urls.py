from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name='cart'
urlpatterns = [
    url(r'^cart/$',views.cart,name="cart"),
    url(r'^deleteHander/$', views.deleteHander, name="deleteHander"),
    url(r'^place_order/$', views.place_order, name="place_order"),
    url(r'^place_hander/$', views.place_hander, name="place_hander"),
]
