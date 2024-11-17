from django.urls import path
from . import views


urlpatterns = [
    # Standaard URL's
    path('', views.index, name='index'),
    path('exportdata/', views.exportdata, name='exportdata'),
    
    
    # Datacollection URL's
    path('datacollection/', views.datacollection_view, name='datacollection'),  # Data list page
    path('datacollection/new_record/', views.new_record_view, name='new_record'),  # Form page for adding new record
    path('datacollection/edit/<int:pk>/', views.edit_record_view, name='edit_record'),  # URL for editing a record
    path('datacollection/biotic/<int:pk>/', views.biotic, name='biotic'),  # Record biotic page
    
    # Fykelocations URL's
    path('fykelocations/', views.fykelocations, name='fykelocations'),
    path('fykelocations/new_location/', views.new_location, name='new_location'),
    path('fykelocations/edit_location/<int:pk>/', views.edit_location, name='edit_location'), 
    
    # Fishdetails URL's
    path('fishdetails/', views.fishdetails, name='fishdetails'),
    path('fishdetails/live-species-search/', views.species_search, name='species_search'),
]
