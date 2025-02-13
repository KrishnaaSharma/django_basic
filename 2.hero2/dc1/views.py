
from django.http import HttpResponse

# Create your views here.
def spiderman2(request):
    return HttpResponse('<h1>I am is spiderman2</h1>')

def ironman2(request):
    return HttpResponse('<h1>I am is IromMan2</h1>')