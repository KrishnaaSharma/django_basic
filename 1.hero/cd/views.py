
from django.http import HttpResponse
# Create your views here.

def spiderman(request):
    return HttpResponse('<h1>I am is spiderman</h1>')

def ironman(request):
    return HttpResponse('<h1>I am is IromMan</h1>')