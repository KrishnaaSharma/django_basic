from django.shortcuts import render

# Create your views here.


def ironman(request):
    return render(request, 'mervel/ironman.html')

def superman(request):
    return render(request, 'mervel/superman.html')