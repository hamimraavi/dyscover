from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search/.*$', views.show_restaurants, name='show_restaurants'),
]
