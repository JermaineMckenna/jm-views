
from django.db import models
from services.models import Service


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=120,
        blank=True,
        help_text="Client role or company (optional)",
    )
    quote = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} – {self.quote[:40]}..."


class PortfolioItem(models.Model):
    PORTFOLIO_TYPE_CHOICES = [
        ("web", "Web & Digital Projects"),
        ("media", "Photography & Media"),
        ("drone", "Drone & Aerial"),
    ]

    CATEGORY_CHOICES = [
        ("design", "Design"),
        ("photo", "Photography"),
        ("video", "Video"),
        ("three_d", "3D & Motion"),
    ]

    COLLECTION_CHOICES = [
        ("web", "Web & Digital Projects"),
        ("photo", "Photography & Video"),
        ("drone", "Drone & Aerial"),
        ("three_d", "3D & Motion"),
        ("branding", "Branding & Visual Design"),
    ]

    title = models.CharField(max_length=200)

    portfolio_type = models.CharField(
        max_length=10,
        choices=PORTFOLIO_TYPE_CHOICES,
        default="media",
    )

    collection = models.CharField(
        max_length=20,
        choices=COLLECTION_CHOICES,
        default="photo",
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    # Optional sub-folder / section (e.g. “Scenic & Coastal Imagery”)
    section = models.CharField(
        max_length=120,
        blank=True,
        help_text=(
            "Optional sub-section, e.g. Portraits & Lifestyle, "
            "Scenic & Coastal Imagery, Events"
        ),
    )

    service = models.ForeignKey(
        Service,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="portfolio_items",
    )

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to="portfolio/")

    external_url = models.URLField(
        blank=True,
        help_text="Optional link to the live site, video or external project page.",
    )

    # NEW: 3 separate homepage toggles
    show_in_photography_highlights = models.BooleanField(
        default=False,
        help_text="Show this item in the homepage ‘Photography highlights’ strip.",
    )

    show_in_drone_highlights = models.BooleanField(
        default=False,
        help_text="Show this item in the homepage ‘Drone & Aerial Footage’ area.",
    )

    show_in_recent_work = models.BooleanField(
        default=False,
        help_text="Show this item in the homepage ‘Recent work’ section.",
    )

    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.title
