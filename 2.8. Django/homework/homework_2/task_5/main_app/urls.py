from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index),    
    path('contact/', views.contact), 
    path('support/', views.support), 
]