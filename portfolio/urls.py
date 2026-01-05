from django.urls import path
from . import views

urlpatterns = [
    # /portfolio/
    path("", views.portfolio_list, name="portfolio_list"),

    # /portfolio/collections/
    path("collections/", views.portfolio_collections, name="portfolio_collections"),

    # /portfolio/collection/photo/  (or web, drone, etc.)
    path("collection/<str:key>/", views.portfolio_collection, name="portfolio_collection"),

    # /portfolio/7/
    path("<int:pk>/", views.portfolio_detail, name="portfolio_detail"),
]