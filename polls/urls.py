from django.conf.urls import url

from . import views

app_name ='polls'
urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote'),
]


