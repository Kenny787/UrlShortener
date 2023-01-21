from django.shortcuts import render

def home(request):
    return render(request, 'test.html')


def createShortURL(request):
    return render(request, 'test.html')


def redirect(request):
    return render(request, 'test.html')


# Create your views here.
