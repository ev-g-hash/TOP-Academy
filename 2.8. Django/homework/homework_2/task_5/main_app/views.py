from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse('Index')
def contact(request):
    return HttpResponse('Contact')
def support(request):
    return HttpResponseRedirect('/contact/')

