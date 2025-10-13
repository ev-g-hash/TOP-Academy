from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('contact/', views.contact, name='contact'),
]