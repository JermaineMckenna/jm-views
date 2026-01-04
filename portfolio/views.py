from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from .models import PortfolioItem, Testimonial


def testimonials(request):
    """
    Simple testimonials page. For now this can just show a
    'coming soon' message or any Testimonial objects you add.
    """
    testimonials_qs = Testimonial.objects.all()
    return render(
        request,
        "testimonials.html",
        {"testimonials": testimonials_qs},
    )


# Nice descriptions for each main folder
COLLECTION_DESCRIPTIONS = {
    "photo": "Portraits, travel photography and event moments from personal and client shoots.",
    "drone": "Selected drone clips and aerial views, captured along the coast and on location.",
    "web": "Web, UI and digital design projects – from landing pages to small web apps.",
    "three_d": "Logo animation tests, motion graphics and 3D experiments.",
    "branding": "Branding, visual identity and design support for small businesses and creators.",
}

# Fixed section “sub-folders” for each collection
COLLECTION_SECTION_LABELS = {
    "photo": [
        "Portraits & Lifestyle",
        "Travel & Scenic",
        "Events & Candid Moments",
        "Documentary & Story-Telling",
    ],
    "drone": [
        "Coastal & Landscape Aerials",
        "Travel & Destination Aerials",
        "Documentary & Story-Driven Clips",
    ],
    "web": [
        "Websites & Landing Pages",
        "Interactive & Experimental Projects",
    ],
    "three_d": [
        "Logo Animations & Idents",
        "Motion Experiments",
    ],
    "branding": [
        "Brand Identity & Collateral",
    ],
}


def portfolio_collections(request):
    """
    Top-level Portfolio page – shows the main 'folders'
    (Drone & Aerial, Photography & Video, etc.).
    """
    raw_collections = (
        PortfolioItem.objects
        .values("collection")
        .annotate(total=Count("id"))
        .order_by("collection")
    )

    label_map = dict(PortfolioItem.COLLECTION_CHOICES)

    collections = []
    for c in raw_collections:
        key = c["collection"]
        collections.append(
            {
                "key": key,
                "label": label_map.get(key, key.title()),
                "total": c["total"],
            }
        )

    return render(
        request,
        "portfolio/portfolio_collections.html",
        {"collections": collections},
    )


def portfolio_collection_detail(request, collection_key):
    """
    Inside a folder – group items into section 'sub-folders'.
    Empty sections still show a heading + 'coming soon'.
    """
    items_qs = (
        PortfolioItem.objects
        .filter(collection=collection_key)
        .select_related("service")
        .order_by("-created_at")
    )
    items = list(items_qs)

    collection_name = dict(PortfolioItem.COLLECTION_CHOICES).get(
        collection_key,
        collection_key.title(),
    )

    collection_description = COLLECTION_DESCRIPTIONS.get(collection_key, "")

    default_sections = COLLECTION_SECTION_LABELS.get(
        collection_key,
        ["All projects"],
    )

    sections = []
    for label in default_sections:
        section_items = [i for i in items if (i.section or "").strip() == label]
        sections.append(
            {
                "label": label,
                "items": section_items,
            }
        )

    return render(
        request,
        "portfolio/portfolio_collection_detail.html",
        {
            "collection_name": collection_name,
            "collection_key": collection_key,
            "collection_description": collection_description,
            "sections": sections,
        },
    )


def portfolio_detail(request, pk):
    """
    Single project page.
    """
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, "portfolio/portfolio_detail.html", {"item": item})