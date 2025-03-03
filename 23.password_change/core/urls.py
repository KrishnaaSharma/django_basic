from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    path('login/', views.log_in, name='log_in'),
    path('success/', views.success, name='success'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.log_out, name='logout'),
    path('pcf/', views.pcf, name='pcf'),
    path('spf/', views.spf, name='spf'),
]
