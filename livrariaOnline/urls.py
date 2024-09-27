from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeSearch, name="homeSearch"),
    path('login/', views.loginUser, name='loginUser'),
    path('createUser/', views.createUser, name="createUser"),
    path('bookView/<str:book_id>', views.bookView, name="bookView"),
    #path('cart/', views.cartView, name='cartView'),
    path('cartAdd/<str:book_id>', views.cartAdd, name='cartAdd')
]