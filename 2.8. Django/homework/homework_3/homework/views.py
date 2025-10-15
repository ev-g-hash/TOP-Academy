from django.shortcuts import render
from django.template.response import TemplateResponse

#-----------------------------------------------задача 1----------------------------
def index(request):
    return render(request, 'homework/index.html')

#-----------------------------------------------задача 2----------------------------
# def index(request):
#     return TemplateResponse(request, 'homework/index.html')

#-----------------------------------------------задача 3----------------------------
def contacts(request):
    name_fone = 'Телефон'
    fone = '+79123456789'
    name_mail = 'E-mail'
    mail = 'admin@email.com'

    data = {'name_fone':name_fone, 'fone':fone, 'name_mail':name_mail, 'mail':mail}

    return render(request, 'homework/contacts.html', data)

#-----------------------------------------------задача 4, 5----------------------------
def profile_1(request):

    name_1 = 'Дмитрий'
    age_1 = 39
    phone_1 = '+79123456789'
    email_1 = 'dmitry@email.com'

    data_1 = {'name_1':name_1, 'age_1':age_1, 'phone_1':phone_1, 'email_1':email_1}

    return render(request, 'homework/profile.html', data_1) 

#-----------------------------------------------задача 6----------------------------
def profile(request):   
    
    name = request.GET.get('name')
    age = request.GET.get('age')
    phone = request.GET.get('phone')
    email = request.GET.get('email')

    data = {'name':name, 'age':age, 'phone':phone, 'email':email}
        
    return render(request, 'homework/profile.html', data)     
      

# для GET запроса чтобы не вводить в строке:
#  (    http://127.0.0.1:8000/profile/?name=John&age=39&phone=+79123456789&email=dmitry@email.com   )


