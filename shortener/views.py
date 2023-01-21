from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def createShortURL(request):
    return render(request, 'base.html')


def redirect(request):
    return render(request, 'base.html')


# Create your views here.
