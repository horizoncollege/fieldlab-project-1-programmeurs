from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('species_list/', views.species_list, name='species_list'),
    path('fishprogrammes/', views.fishprogrammes, name='fishprogrammes'),
    path('fishlocations/', views.fishlocations, name='fishlocations'),
]