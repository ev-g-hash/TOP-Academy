from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Главная PBigCiti',
        'content': 'Подарок в большом',
        'content_1': 'городе',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'PBigCiti - О нас',
        'content': 'О нас',
        'text_on_page': 'Подарок в большом городе'
    }
    return render(request, 'main/about.html', context)





