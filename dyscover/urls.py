from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^.*$', views.show_restaurants, name='show_restaurants'),
    url(r'^$', views.index, name='index'),
    ]
