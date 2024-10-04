from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.options_view, name='options'),
]
