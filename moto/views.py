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


def get_cats(request, cat_id):
    mot = Moto.objects.filter(cats_id=cat_id)
    cats = Cats.objects.get(pk=cat_id)
    category = Cats.objects.all()
    context = {
        'mot': mot,
        'category': category,
        'cats': cats
    }
    return render(request, 'moto/cats.html', context)  #template name='moto/cats.html'


def about_page(request):
    return render(request, 'moto/about.html')


def add_moto(request):
    return render(request, 'moto/add_moto.html')