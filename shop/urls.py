from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.product_list_api, name='product_list_api'),
    path('api/products/<int:pk>/', views.product_detail_api, name='product_detail_api'),
]