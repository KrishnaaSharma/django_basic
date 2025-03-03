from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import Register
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        mf= Register(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'Registration Successful ! ')
            return redirect('/')
    else:
        mf = Register()
    return render(request,'core/index.html',{'mf':mf})