from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('species_list/', views.species_list, name='species_list'),
    path('species/<int:species_id>/', views.species_detail, name='species_detail'),
    path('species/edit/<int:species_id>/', views.species_edit, name='species_edit'),
    path('fishprogrammes/', views.fishprogrammes, name='fishprogrammes'),
    path('fishlocations/', views.fishlocations, name='fishlocations'),
]
