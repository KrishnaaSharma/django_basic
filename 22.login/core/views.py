from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . forms import Register
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        mf= Register(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'Registration Successful ! ')
            return redirect('/profile/')
    else:
        mf = Register()
    return render(request,'core/index.html',{'mf':mf})


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = AuthenticationForm(request,data=request.POST)
            if mf.is_valid():
                un = mf.cleaned_data['username']
                pw = mf.cleaned_data['password']
                user=authenticate(username=un,password=pw)
                if user is not None:
                    login(request,user)
                    # return HttpResponse('login successful!')
                    # return render(request,'core/success.html')
                    return redirect('/profile/')
        else:
            mf=AuthenticationForm()
        return render(request,'core/log_in.html',{'mf':mf})
    else:
        return redirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'core/profile.html')
    else:
        return redirect('/login/')

def log_out(request):
    logout(request)
    return redirect('/login/')

def success(request):
    return render(request,'core/success.html')