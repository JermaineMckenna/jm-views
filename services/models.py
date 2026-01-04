from django.db import models


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('design', 'Design'),
        ('photo', 'Photography'),
        ('video', 'Video & Editing'),
        ('three_d', '3D & Motion'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField(blank=True)
    starting_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
