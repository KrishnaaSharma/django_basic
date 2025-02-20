from django.shortcuts import render
from . forms import MarvelForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            print(mf.cleaned_data['name'])
            print(mf.cleaned_data['password'])
            print(mf.cleaned_data['confirm_password'])
            mf =MarvelForm()
    else:
        mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})