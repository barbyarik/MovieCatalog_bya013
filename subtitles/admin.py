from django.contrib import admin
from .models import Subtitle

class SubtitleAdmin(admin.ModelAdmin):
    list_display = ('film', 'start_time', 'text')
    list_filter = ('film',)
    ordering = ('film__name', 'start_time')
    search_fields = ('film__name', 'text')

admin.site.register(Subtitle, SubtitleAdmin)