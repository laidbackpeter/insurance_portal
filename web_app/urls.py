from django.conf.urls import url
from web_app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]