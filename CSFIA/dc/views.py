from django.shortcuts import render

# Create your views here.

def batman(request):
    return render(request, 'dc/batman.html')

def spiderman(request):
    return render(request, 'dc/spiderman.html')