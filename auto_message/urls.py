from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path(r'api/', views.report),
    path(r'diy_send/', views.DIYMessageSend.as_view()),
]
