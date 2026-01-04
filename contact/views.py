from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ContactRequestForm
from services.models import Service


def contact(request):
    service_id = request.GET.get('service')
    initial = {}

    service_obj = None
    if service_id:
        service_obj = get_object_or_404(Service, pk=service_id)
        initial['service'] = service_obj

    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for your enquiry. I'll review your brief and get back to you as soon as possible."
            )
            return redirect('home')
    else:
        form = ContactRequestForm(initial=initial)

    context = {
        'form': form,
        'selected_service': service_obj,
    }
    return render(request, 'contact/contact.html', context)

