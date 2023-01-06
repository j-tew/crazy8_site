from django.contrib import admin
from .models import Gig

# Register your models here.

@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ('artist', 'date', 'start_time', 'end_time')
    list_filter = ('date',)
    ordering = ('-date',)
    search_fields = ('date', 'artist')