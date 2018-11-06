from django.conf.urls import url
from . import views

app_name = 'identitys'
urlpatterns = [
        url(r'^$', views.index, name='index'),
       # url(r'^$', views.inputdata, name='inputdata'),
       # url(r'^$', views.result, name='result'),
       # url(r'^$', views.searching, name='searching'),
        ]
