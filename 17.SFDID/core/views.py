from django.shortcuts import render,redirect
from .forms import MarvelForm
from .models import MarvelModel

# Create your views here.
def index(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            nm= mf.cleaned_data['name']
            hn= mf.cleaned_data['heroic_name']
            MarvelModel(name=nm,heroic_name=hn).save()
            return redirect('/')
    else:
        mf=MarvelForm()
    return render(request,'core/index.html',{'mf':mf})