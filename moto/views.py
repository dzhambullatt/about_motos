from django.shortcuts import render
from django.http import HttpResponse


def news(request):
    return HttpResponse('<p>hello world</p>')


def about(request):
    return HttpResponse('<h1>about page</h1>')