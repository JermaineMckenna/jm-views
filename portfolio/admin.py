from django.contrib import admin
from .models import PortfolioItem
from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "created_at", "is_featured")
    list_filter = ("is_featured", "created_at")
    search_fields = ("name", "role", "quote")


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'portfolio_type',
        'collection',
        'category',
        'service',
        'section',
        'is_featured',
        'created_at',
    )
    list_filter = (
        'portfolio_type',
        'collection',
        'category',
        'is_featured',
        'created_at',
    )
    search_fields = ('title', 'description', 'external_url')

