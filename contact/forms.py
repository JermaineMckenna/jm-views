from django import forms
from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = [
            'name',
            'email',
            'phone_number',
            'budget',
            'timeframe',
            'contact_method',
            'service',
            'reference_url',
            'message',
        ]
        widgets = {
            'service': forms.HiddenInput(),
            'message': forms.Textarea(attrs={'rows': 5}),
        }