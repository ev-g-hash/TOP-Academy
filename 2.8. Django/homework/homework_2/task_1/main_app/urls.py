from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('products/new/', views.new),
    path('products/top/', views.top),
]