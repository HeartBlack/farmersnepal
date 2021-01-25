from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductApi, name = 'ProductApi'),
    path('vendor/', views.Vendor_details, name = 'Post_product'),
    path('vendor/<int:pk>/', views.Vendor_details, name = 'Post_product'),

     
] 