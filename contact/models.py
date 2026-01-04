from django.db import models
from services.models import Service


class ContactRequest(models.Model):
    BUDGET_CHOICES = [
        ('under_250', 'Under £250'),
        ('250_500', '£250 – £500'),
        ('500_1000', '£500 – £1,000'),
        ('1000_2000', '£1,000 – £2,000'),
        ('over_2000', 'Over £2,000'),
        ('unsure', "I'm not sure yet"),
    ]

    TIMEFRAME_CHOICES = [
        ('asap', 'ASAP'),
        ('two_weeks', 'Within 2 weeks'),
        ('month', 'Within a month'),
        ('flexible', 'Flexible / not urgent'),
    ]

    CONTACT_METHOD_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('either', 'Email or phone'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=True)
    service = models.ForeignKey(
        Service,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='contact_requests',
    )
    budget = models.CharField(
        max_length=20,
        choices=BUDGET_CHOICES,
        default='unsure',
    )
    timeframe = models.CharField(
        max_length=20,
        choices=TIMEFRAME_CHOICES,
        default='flexible',
    )
    contact_method = models.CharField(
        max_length=10,
        choices=CONTACT_METHOD_CHOICES,
        default='email',
    )
    reference_url = models.URLField(
        blank=True,
        help_text='Optional link to inspiration, social media or similar work.'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.service:
            return f"{self.name} – {self.service.name}"
        return self.name
