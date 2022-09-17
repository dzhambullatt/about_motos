from django.urls import path
from .views import *

urlpatterns = [
    path('', news),
    path('cats_url/<int:cat_id>/', get_cats),
]