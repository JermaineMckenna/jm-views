from django.contrib import admin
from .models import PortfolioItem, Testimonial


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    # Columns in the list view
    list_display = (
        "title",
        "portfolio_type",
        "collection",
        "category",
        "section",
        "is_featured",
        "show_on_homepage",
        "created_at",
    )

    # Filters on the right-hand side
    list_filter = (
        "portfolio_type",
        "collection",
        "category",
        "section",
        "is_featured",
        "show_on_homepage",
        "created_at",
    )

    search_fields = ("title", "section", "description")

    # Fields + layout in the edit form
    fields = (
        "title",
        ("portfolio_type", "collection", "category"),
        "section",
        "service",
        "description",
        "image",
        "external_url",
        ("is_featured", "show_on_homepage"),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_featured", "created_at")
    list_filter = ("is_featured", "created_at")
    search_fields = ("name", "role", "quote")

