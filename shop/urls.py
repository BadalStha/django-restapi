from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('api/products/', views.product_list_api, name='product_list_api'),
    path('api/products/<int:pk>/', views.product_detail_api, name='product_detail_api'),
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]