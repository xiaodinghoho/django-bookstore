from django.conf.urls import include, url
from . import views

app_name='detail'
urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url('^detail/$',views.detail,name='detail'),
    url('^addcart/$',views.addcart,name='addcart'),
    url('^comment([0-9]*)/$',views.comment,name='comment'),
]


