from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h1>')

def catalog(request):
    return HttpResponse('<h1>Каталог</h1>')

def contact(request):
    return HttpResponse('<h1>Контакты</h1>')