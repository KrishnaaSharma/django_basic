from django.urls import path
from mervel import views

urlpatterns = [
    path('ironman/',views.ironman),
    path('spiderman/',views.spiderman),
]