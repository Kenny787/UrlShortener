from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_short_url, name='create'),
    path('<str:url>', redirect, name='redirect')
]