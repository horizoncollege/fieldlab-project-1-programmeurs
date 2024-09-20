from django.urls import path
from . import views

urlpatterns = [
    path('adminMenu/', views.admin_menu_view, name='adminMenu'),
]