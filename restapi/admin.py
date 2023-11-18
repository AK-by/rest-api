from django.contrib import admin
from . models import SimpleMessages

@admin.register(SimpleMessages)
class SimpleMessagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'message',
        'created',
        'image',
    )
    sortable_by = (
        'id',
        'title',
        'message',
        'created',
    )
    search_fields = (
        'id',
        'title',
        'message',
        'created',
    )
    list_editable = (
        'title',
        'message',
    )
    date_hierarchy = 'created'
