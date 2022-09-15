from django.shortcuts import render
from django.http import HttpResponse

from .models import Moto


def news(request):
    mot = Moto.objects.order_by('-time_create')
    context = {
        'mot': mot,
        'title': 'title'
    }
    return render(request, 'moto/index.html', context)


def about(request):
    return HttpResponse('<h1>about page</h1>')