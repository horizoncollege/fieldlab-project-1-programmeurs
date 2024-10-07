from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LoginSysteem.urls')),
    path('', include('adminMenu.urls')),
    path('fyke/', include('fyke.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('options/', include('optionsApp.urls')),
    path('help/', include('helpApp.urls')),
]
