from django.shortcuts import render

# Create your views here.


def spiderman(request):
    return render(request, 'mervel/spiderman.html')


def batsman(request):
    return render(request, 'mervel/batsman.html')