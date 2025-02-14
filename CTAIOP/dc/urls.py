from django.urls import path
from . import views


urlpatterns = [
    path('ironman/',views.ironman),
    path('superman/',views.superman),
]
