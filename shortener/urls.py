from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortURL, name='create'),
    path('<str:url>', redirect, name='redirect')
]