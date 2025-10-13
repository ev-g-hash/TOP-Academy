from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная</h1>')

def accounts(request, name='NoName', age=0):
    return HttpResponse(f'Имя: {name}, Возраст: {age}')

def home(request):
    return HttpResponse('<h2>Домашняя страница</h2>')

def message(request, category='Програмирование', subcategory='Python', theme='Django 4', number=12):
    return HttpResponse(f'''
    <h2>Сообщение</h2>
        <ul>
            <li>Категория: {category}</li>
            <li>Подкатегория: {subcategory}</li>
            <li>Тема: {theme}</li>
            <li>Номер сообщения: {number}</li>
        </ul> 
''')


