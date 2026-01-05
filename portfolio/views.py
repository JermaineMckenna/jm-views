from django.shortcuts import render, get_object_or_404
from .models import PortfolioItem, Testimonial


def portfolio_list(request):
    """
    Renders portfolio_list.html

    Shows:
      - web_items: items with portfolio_type = 'web'
      - media_items: everything else (photo, video, drone, 3D)
    """
    web_items = PortfolioItem.objects.filter(portfolio_type="web")
    media_items = PortfolioItem.objects.exclude(portfolio_type="web")

    context = {
        "web_items": web_items,
        "media_items": media_items,
    }
    return render(request, "portfolio/portfolio_list.html", context)


def portfolio_collections(request):
    """
    Renders portfolio_collections.html

    We build a simple list of collections like:
    [
      {"key": "photo", "label": "Photography & Video", "total": 5},
      ...
    ]
    """
    all_items = PortfolioItem.objects.all()
    collections = []

    for key, label in PortfolioItem.COLLECTION_CHOICES:
        collections.append(
            {
                "key": key,
                "label": label,
                "total": all_items.filter(collection=key).count(),
            }
        )

    context = {
        "collections": collections,
    }
    return render(request, "portfolio/portfolio_collections.html", context)


def portfolio_collection(request, key):
    """
    Renders a single collection page, grouping items by `section`
    (e.g. Portraits & Lifestyle, Scenic & Coastal Imagery).
    """
    items = PortfolioItem.objects.filter(collection=key)

    # Group by section
    sections_map = {}
    for item in items:
        section_name = item.section or "Other"
        sections_map.setdefault(section_name, []).append(item)

    # Transform to a list that’s easier to use in templates
    sections = [
        {"name": name, "items": item_list}
        for name, item_list in sections_map.items()
    ]

    collection_label = dict(PortfolioItem.COLLECTION_CHOICES).get(key, key)

    context = {
        "collection_key": key,
        "collection_label": collection_label,
        "sections": sections,
    }
    return render(request, "portfolio/portfolio_collection.html", context)


def portfolio_detail(request, pk):
    """
    Single project detail page.
    """
    item = get_object_or_404(PortfolioItem, pk=pk)
    context = {
        "item": item,
    }
    return render(request, "portfolio/portfolio_detail.html", context)


def testimonials(request):
    """
    Optional: testimonials list page, in case you add a template for it later.
    Not currently wired in urls.py, but harmless to have.
    """
    testimonials_qs = Testimonial.objects.filter(is_featured=True)
    context = {"testimonials": testimonials_qs}
    return render(request, "portfolio/testimonials.html", context)