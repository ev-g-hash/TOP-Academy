from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - каталог",
        "goods": [
            {
                "image": "deps/images/goods/14.jpg",
                "name": "Обложка на паспорт",
                "description": "Обложка на паспорт, мужская, ручная работа",
                "price": 3000,
            },
            {
                "image": "deps/images/goods/2.jpg",
                "name": "Чайный столик и два стула",
                "description": "Набор из стола и двух стульев в минималистическом стиле.",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/3.jpg",
                "name": "Двухспальная кровать",
                "description": "Кровать двухспальная с надголовником и вообще очень ортопедичная.",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/4.jpg",
                "name": "Кухонный стол с раковиной",
                "description": "Кухонный стол для обеда с встроенной раковиной и стульями.",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/5.jpg",
                "name": "Кухонный стол с встройкой",
                "description": "Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/15.jpg",
                "name": "Угловой диван для гостинной",
                "description": "Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/7.jpg",
                "name": "Прикроватный столик",
                "description": "Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/8.jpg",
                "name": "Диван обыкновенный",
                "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/9.jpg",
                "name": "Стул офисный",
                "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/10.jpg",
                "name": "Растение",
                "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/11.jpg",
                "name": "Цветок стилизированный",
                "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
                "price": 00.00,
            },
            {
                "image": "deps/images/goods/12.jpg",
                "name": "Прикроватный столик",
                "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
                "price": 00.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
