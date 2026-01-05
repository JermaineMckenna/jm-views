from django.shortcuts import render
from services.models import Service
from portfolio.models import PortfolioItem


def index(request):
    # Services for the “Featured services” section
    featured_services = Service.objects.all()[:3]

    # Photography highlights strip
    homepage_photos = (
        PortfolioItem.objects.filter(show_in_photography_highlights=True)
        .order_by("-created_at")[:3]
    )

    # Recent work cards
    recent_work = (
        PortfolioItem.objects.filter(show_in_recent_work=True)
        .order_by("-created_at")[:3]
    )

    # Drone items (we can hook these into the drone section later if you like)
    homepage_drone_items = (
        PortfolioItem.objects.filter(show_in_drone_highlights=True)
        .order_by("-created_at")[:3]
    )

    context = {
        "featured_services": featured_services,
        "homepage_photos": homepage_photos,
        "recent_work": recent_work,
        "homepage_drone_items": homepage_drone_items,
    }
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html")