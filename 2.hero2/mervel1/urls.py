from django.urls import path
from . import views

urlpatterns = [
    path('superman2/', views.superman2),
    path('batsman2/', views.batsman2),
]