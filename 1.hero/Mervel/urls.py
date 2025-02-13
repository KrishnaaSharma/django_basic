from django.urls import path
from . import views

urlpatterns = [
    path('superman/', views.superman),
    path('batsman/', views.batsman),
]