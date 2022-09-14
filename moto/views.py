from django.shortcuts import render
from django.http import HttpResponse


def news(request):
    return render(request, 'moto/index.html')


def about(request):
    return HttpResponse('<h1>about page</h1>')