from django.urls import path
from . import views


urlpatterns = [
    # Page URL's
    path('', views.index, name='index'),
    path('datacollection/', views.datacollection_view, name='datacollection'),  # Data list page
    path('fishdetails/', views.fishdetails, name='fishdetails'),
    path('fykelocations/', views.fykelocations, name='fykelocations'),
    path('exportdata/', views.exportdata, name='exportdata'),
    
    
    # Data URLS's
    path('datacollection/new_record/', views.new_record_view, name='new_record'),  # Form page for adding new record
]