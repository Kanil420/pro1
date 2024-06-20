from django.shortcuts import render
from django.http import HttpResponse



def telugu(request):
    return HttpResponse('this is telugu movies')


def hindi(request):
    return HttpResponse('this is a hindi ')

# Create your views here.
