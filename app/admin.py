from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'answer', 'created')
    list_display_links = ('name', 'email', 'phone', 'message', 'answer', 'created')


