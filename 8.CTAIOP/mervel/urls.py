from django.urls import path
from . import views


urlpatterns = [
    path('spiderman/',views.spiderman),
    path('batsman/',views.batsman),
]
