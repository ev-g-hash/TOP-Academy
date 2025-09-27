from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Подарок в большом',
        'content_1': 'городе' 
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том какой классный магазин'
    }
    return render(request, 'main/about.html', context)





