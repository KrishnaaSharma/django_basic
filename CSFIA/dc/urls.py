from django.urls import path
from . import views

urlpatterns = [
    path('batman/', views.batman),
    path('spiderman/', views.spiderman),
]
