from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework.authtoken import views as rest_views
from rest_framework import routers

router  = routers.SimpleRouter()
router.register(r'incomes/' , views.IncomeViewSet)


app_name = 'accountRest'
urlpatterns = [
    path('get_token', views.CustomAuthToken.as_view() , name= 'obtain_token'),
    path('test_auth' , views.Test.as_view() , name = 'test'),
]

urlpatterns += router.urls
