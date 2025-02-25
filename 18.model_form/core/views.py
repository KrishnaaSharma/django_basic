from django.shortcuts import render,redirect
from .forms import MarvelForm, DcForm
from .models import MarvelModel, DcModel

# Create your views here.
def index(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/')
    else:
        mf=MarvelForm()
    return render(request,'core/index.html',{'mf':mf})


def dc(request):
    if request.method == 'POST':
        dc = DcForm(request.POST)
        if dc.is_valid():
            dc.save()
            return redirect('/dc/')
        
    else:
        dc = DcForm()
    return render(request, 'core/dc.html',{'dc':dc})