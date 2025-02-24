from django.shortcuts import render,redirect
from .forms import MarvelForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            print(f"Name is {mf.cleaned_data['name']}")
            print(f"Heoric Name is {mf.cleaned_data['heroic_name']}")
            return redirect('/')
    else:
        mf=MarvelForm()
    return render(request,'core/index.html',{'mf':mf})