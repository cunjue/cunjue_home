
from django.contrib import admin
from django.urls import path

from c_1 import views

app_name='c_1'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('haha/', views.haha,name='haha'),
    path('register',views.register,name='register'),
]
