from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name = 'home'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('abc/',views.order_place, name ='abc'),
    path('dashboard/',views.order_item, name ='dashboard'),
    path('allproducts/',views.allproducts,name='allproducts'),
    path('about/',views.aboutus, name ='aboutus'),
    path('contactus/',views.contactus,name='contactus'),

] 