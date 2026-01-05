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
        "show_in_photography_highlights",
        "show_in_drone_highlights",
        "show_in_recent_work",
        "created_at",
    )

    # Filters on the right-hand side
    list_filter = (
        "portfolio_type",
        "collection",
        "category",
        "section",
        "is_featured",
        "show_in_photography_highlights",
        "show_in_drone_highlights",
        "show_in_recent_work",
        "created_at",
    )

    search_fields = ("title", "section", "description")

    # Nicely grouped sections in the edit form
    fieldsets = (
        ("Basic info", {
            "fields": (
                "title",
                ("portfolio_type", "collection", "category"),
                "section",
                "service",
                "description",
            )
        }),
        ("Media", {
            "fields": ("image", "external_url"),
        }),
        ("Homepage placement", {
            "fields": (
                "is_featured",
                "show_in_photography_highlights",
                "show_in_drone_highlights",
                "show_in_recent_work",
            ),
            "description": "Choose where this project should appear on the home page.",
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_featured", "created_at")
    list_filter = ("is_featured", "created_at")
    search_fields = ("name", "role", "quote")
