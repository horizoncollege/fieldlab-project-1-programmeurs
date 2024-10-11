from django.urls import path
from . import views
# from .views import adminMenu

urlpatterns = [
    # Root URL
    path('', views.adminMenu, name='adminMenu'),

    # Admin Menu URL
    path('adminMenu/', views.admin_menu_view, name='adminMenuView'),

    # Admin Menu User URL
    path('adminMenuUser/', views.admin_menu_user, name='adminMenuUser'),
]