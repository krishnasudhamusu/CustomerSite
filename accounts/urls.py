from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/',views.logoutUser,name='logout'),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('create-order/<str:pk>/', views.createOrder, name='create-order'),
    path('update-order/<str:pk>/', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),
]
