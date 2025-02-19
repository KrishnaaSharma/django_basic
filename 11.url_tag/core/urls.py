from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/',views.about),
    path('aboutjuig/',views.about),
    path('about123/',views.about, name = 'aboutus')
]
