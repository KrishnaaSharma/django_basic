from django.shortcuts import render
from .models import MarvelModel
# Create your views here.


def index(request):
    mf=MarvelModel.objects.all()
    return render(request,'core/index.html',{'mf':mf})