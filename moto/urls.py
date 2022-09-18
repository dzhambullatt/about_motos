from django.urls import path
from .views import *

urlpatterns = [
    path('', news, name='home'),
    path('cats_url/<int:cat_id>/', get_cats, name='cats'),
]