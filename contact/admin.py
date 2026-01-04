from django.contrib import admin
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
        'service',
        'budget',
        'timeframe',
        'contact_method',
        'created_at',
    )
    list_filter = ('service', 'budget', 'timeframe', 'contact_method', 'created_at')
    search_fields = ('name', 'email', 'phone_number', 'message', 'reference_url')