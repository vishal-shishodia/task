from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *
urlpatterns = [
    path('', index,name="index"),
    path('register/',CreateUser,name="register"),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('additem/',AddItem,name='additem'),
    path('edititem/<str:pk>/',EditItem,name='edititem'),
    path('delete/<str:pk>/',DeleteItem,name='delete'),
    path('merchanthome/',MerchantHome,name='merchanthome'),
]