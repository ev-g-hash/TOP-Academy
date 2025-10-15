from django.urls import path
from homework import views


urlpatterns = [
    #----------------------------------------задача 1------------------------------
    path('', views.index, name='index'),
    path('contacts/', views.contacts),  
    path('user/profile/', views.profile_1),  
    path('profile/', views.profile),  
]