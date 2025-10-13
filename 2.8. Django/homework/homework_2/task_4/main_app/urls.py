from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.index), 
    path('about/', views.about), 
    path('contact/', views.contact), 
    path('details/', views.details), 
]