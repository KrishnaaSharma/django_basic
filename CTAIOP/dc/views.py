from django.shortcuts import render

# Create your views here.

def ironman(request):
    return render(request, 'dc/ironman.html')


def superman(request):
    return render(request, 'dc/superman.html')