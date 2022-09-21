from django import forms
from .models import Cats


class MotoForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField()
    is_published = forms.BooleanField()
    cats = forms.ModelChoiceField(queryset=Cats.objects.all())