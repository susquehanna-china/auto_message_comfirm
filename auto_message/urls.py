from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('index/', views.index),
    path(r'api/', views.report),
]
