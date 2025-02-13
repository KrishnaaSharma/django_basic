from django.urls import path
from . import views

urlpatterns = [
    path('spiderman2/', views.spiderman2),
    path('ironman2/', views.ironman2)
]