from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeSearch, name="homeSearch"),
    path('login/', views.login, name="login")
]