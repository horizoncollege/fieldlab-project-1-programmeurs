from django.urls import path
from . import views
from .views import adminMenu

urlpatterns = [
    # Root URL
    path('', views.adminMenu, name='adminMenu'),

    # Admin Menu URL
    path('adminMenu/', views.admin_menu_view, name='adminMenuView'),

    # Admin Menu User URL
    path('adminMenuUser/<int:pk>/', views.admin_menu_user, name='adminMenuUser'),

    # Admin Menu New User URL
    path('adminMenuNewUser/', views.admin_menu_new_user, name='adminMenuNewUser'),
]