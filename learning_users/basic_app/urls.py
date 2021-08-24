from django.conf.urls import url
from django.urls import path
from basic_app import views


# TEMPLATE URLS!

app_name = 'basic_app'  # matching the application name

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]
