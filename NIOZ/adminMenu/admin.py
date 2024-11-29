from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'realName', 'collectlocation', 'yearFrom', 'yearUntil')
    search_fields = ('user__username', 'realName', 'collectlocation')
    list_filter = ('yearFrom', 'yearUntil')
    ordering = ('user',)

admin.site.register(Person, PersonAdmin)