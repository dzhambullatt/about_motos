from django.urls import path
from .views import *

urlpatterns = [
    path('', news, name='home'),
    path('cats_url/<int:cat_id>/', get_cats, name='cats'),
    path('about/', about_page, name='about'),
    path('add_moto/', add_moto, name='add_moto'),
    path('moto/<int:moto_id>/', view_moto, name='view_moto'),
]
