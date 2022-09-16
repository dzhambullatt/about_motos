from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def news(request):
    mot = Moto.objects.order_by('-time_create')
    cats = Cats.objects.all()
    context = {
        'mot': mot,
        'title': 'Мотоциклы',
        'cats': cats,
    }
    return render(request, 'moto/index.html', context)


def about(request):
    return HttpResponse('<h1>about page</h1>')