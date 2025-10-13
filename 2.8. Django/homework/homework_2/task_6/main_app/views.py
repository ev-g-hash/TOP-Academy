from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect

def index(request):
    return HttpResponse('Index')
def about(request):
    return HttpResponsePermanentRedirect('/')
