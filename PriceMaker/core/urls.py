from django.urls import path
from .import views


urlpatterns = [
    path('', views.calculate_price, name='calculate_price'),
    path('price_detail/<int:pk>/', views.price_detail, name='price_detail'),
]