from django.shortcuts import render
from services.models import Service
from portfolio.models import PortfolioItem


def index(request):
    # Up to 3 featured services
    featured_services = Service.objects.all()[:3]

    # Up to 3 photography items that are marked to show on homepage
    photography_items = (
        PortfolioItem.objects
        .filter(portfolio_type="media", show_on_homepage=True)
        .order_by("-created_at")[:3]
    )

    # Recent work (all types)
    recent_work = PortfolioItem.objects.order_by("-created_at")[:3]

    context = {
        "featured_services": featured_services,
        "recent_work": recent_work,
        "photography_items": photography_items,
    }
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html")