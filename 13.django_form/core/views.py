from django.shortcuts import render
from .form import MarvelForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        mf=MarvelForm(request.POST)
        if mf.is_valid():
            nm = mf.cleaned_data['name']
            hn = mf.cleaned_data['heroic_name']
            print(nm)
            print(hn)
            mf=MarvelForm()
    else:
        mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})
