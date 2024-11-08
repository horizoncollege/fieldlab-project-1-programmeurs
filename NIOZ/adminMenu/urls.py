from django.urls import path
from . import views
from .views import adminMenu

urlpatterns = [
    # Admin Menu URL
    path('adminMenu/', views.users_view, name='users_view'),

    # Admin Menu User URL
    path('user/<int:pk>/', views.userinfo_view, name='userinfo_view'),

    # Admin Menu New User URL
    path('new_user/', views.new_user, name='new_user'),
]