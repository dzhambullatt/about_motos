from django import forms
from .models import Cats


class MotoForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название')
    content = forms.CharField(label='Контент')
    is_published = forms.BooleanField(label='Опубликовано', initial=True)
    cats = forms.ModelChoiceField(empty_label='Выбрать Категорию', queryset=Cats.objects.all(), label='Категория')

