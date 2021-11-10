from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_user),
    path('login', views.login_user),
    path('detales', views.detales),
    path('logout', views.logout),
]