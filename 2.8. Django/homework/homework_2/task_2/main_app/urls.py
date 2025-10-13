from django.urls import path, include
from main_app import views

product_urlpatterns = [
    path('', views.products), 
    path('comments/', views.comments), 
    path('questions/', views.questions),
]

urlpatterns = [
    path('', views.index), 
    path('products/<int:id>/', include(product_urlpatterns)), 
]