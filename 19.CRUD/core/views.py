from django.shortcuts import render,redirect
from .forms import MarvelForm
from .models import MarvelModel 

# Create your views here.
def index(request):
    if request.method == 'POST':
        mf= MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect ('/')
        
    else:
        mf= MarvelForm()
        mm= MarvelModel.objects.all()
    return render(request, 'core/index.html', {'mm':mm, 'mf': mf})


def delete_avenger(request, id):
    mm = MarvelModel.objects.get(pk=id)
    mm.delete()
    return redirect('/')
    

def update_avenger(request, id):
    if request.method == 'POST':
        mm = MarvelModel.objects.get(pk=id)
        mf= MarvelForm(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()
            return redirect('/')
        
    else:
        mm= MarvelModel.objects.get(pk=id)
        mf=MarvelForm(instance=mm)
    return render(request, 'core/update.html', {'mf':mf})


