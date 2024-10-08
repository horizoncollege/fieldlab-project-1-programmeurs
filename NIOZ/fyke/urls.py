from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datacollection/', views.datacollection, name='datacollection'),
    path('fishdetails/', views.fishdetails, name='fishdetails'),
    path('fykelocations/', views.fykelocations, name='fykelocations'),
    path('exportdata/', views.exportdata, name='exportdata'),
]
