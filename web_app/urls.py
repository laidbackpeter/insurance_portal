from django.conf.urls import url
from web_app import views

urlpatterns = [
    url(r'^$', views.HomePageView, name='index'),
    url(r'^about/$', views.AboutPageView, name='about'),
]