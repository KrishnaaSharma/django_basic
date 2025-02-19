from django.urls import path
from . import views

urlpatterns = [
    path('', views.villain),
    path('hero/',views.hero),
]
