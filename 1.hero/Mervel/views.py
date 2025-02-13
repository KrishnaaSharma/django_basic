
from django.http import HttpResponse
# Create your views here.

def superman(request):
    return HttpResponse ('<h1>I am is superman</h1>')

def batsman(request):
    return HttpResponse ('<h1>I am is batsman</h1>')