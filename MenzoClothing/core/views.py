from django.shortcuts import render
from . models import Pet
# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def products(request):
    dc = Pet.objects.all()
    return render(request,'core/products.html',{'dc':dc})



def product_details(request,id):
    dc= Pet.objects.get(pk=id)
    return render(request,'core/product_details.html',{'dc':dc})