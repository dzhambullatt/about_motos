from django import forms
from .models import Moto


class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['title', 'content', 'is_published', 'cats']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'cats': forms.Select(attrs={'class': 'form-control'})
        }










    # title = forms.CharField(max_length=255, label='Название')
    # content = forms.CharField(label='Контент')
    # is_published = forms.BooleanField(label='Опубликовано', initial=True)
    # cats = forms.ModelChoiceField(empty_label='Выбрать Категорию', queryset=Cats.objects.all(), label='Категория')

