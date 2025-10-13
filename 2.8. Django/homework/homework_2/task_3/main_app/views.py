from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def user(request):
    age = request.GET.get('age')
    name = request.GET.get('name')
    return HttpResponse(f'<h2>Имя: {name}, Возраст: {age}</h2>')

