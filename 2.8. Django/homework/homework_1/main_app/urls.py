from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('accounts/', views.accounts), 
    path('accounts/<str:name>', views.accounts),    
    path('accounts/<str:name>/<int:age>', views.accounts),    
    path('home/', views.home),        
    path('message/', views.message),    
    path('message/<str:category>/<str:subcategory>/<str:theme>/<int:number>', views.message),    
]