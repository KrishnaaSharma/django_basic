from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete_avenger, name='delete'),
    path('update/<int:id>', views.update_avenger, name='update'),
]
