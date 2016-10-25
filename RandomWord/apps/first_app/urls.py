from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.first_app),
    url(r'^generate$', views.generate)
    ]
