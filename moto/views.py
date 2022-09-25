from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .models import *
from .forms import MotoForm


class HomeMoto(ListView):
    model = Moto
    template_name = 'moto/index.html'


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


def view_moto(request, moto_id):
    moto_item = Moto.objects.get(pk=moto_id)
    return render(request, 'moto/view_moto.html', {"moto_item": moto_item})


def about_page(request):
    return render(request, 'moto/about.html')


def add_moto(request):
    if request.method == "POST":
        form = MotoForm(request.POST)
        if form.is_valid():
            moto = form.save()
            return redirect('home')
    else:
        form = MotoForm()
    return render(request, 'moto/add_moto.html', {'form': form})



