from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'accountRest'
urlpatterns = [
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('register', views.RegisterAPIView.as_view() , name='register'),
]
