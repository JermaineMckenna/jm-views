from django.urls import path
from . import views

urlpatterns = [
    # ...existing paths...
    path("testimonials/", views.testimonials, name="testimonials"),
    
    # Folder / collections view
    path('', views.portfolio_collections, name='portfolio_collections'),

    # Items inside a specific folder/collection
    path('collection/<str:collection_key>/', views.portfolio_collection_detail, name='portfolio_collection'),

    # Individual portfolio item detail page
    path('<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
]
