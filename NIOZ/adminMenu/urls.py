from django.urls import path
from . import views
from .views import hardcoded_people_view

urlpatterns = [
    path('adminMenu/', views.admin_menu_view, name='adminMenu'),
]

urlpatterns = [
    path('adminMenu/', hardcoded_people_view, name='people_list'),
]