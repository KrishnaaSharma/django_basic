from django.shortcuts import render

# Create your views here.

def villain(request):
    return render(request, 'core/villain.html', {'villain:': 'gobling'})

def hero(request):
    return render(request,'core/hero.html',{'hero':['captain america','ironman','spiderman','thor','black panther','black widow','hulk']})