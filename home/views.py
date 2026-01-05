from django.shortcuts import render
from services.models import Service
from portfolio.models import PortfolioItem


def index(request):
    featured_services = Service.objects.all()[:3]

    # Items specifically marked to appear in the home photography strip
    homepage_items = (
        PortfolioItem.objects
        .filter(show_on_homepage=True)
        .order_by("-created_at")[:3]
    )

    # Recent work for the bottom grid
    recent_work = PortfolioItem.objects.order_by("-created_at")[:3]

    context = {
        "featured_services": featured_services,
        "recent_work": recent_work,
        "homepage_items": homepage_items,
    }
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html")