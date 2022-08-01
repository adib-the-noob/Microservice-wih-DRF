from scraper.views import get_stock
from django.urls import path, include

urlpatterns = [
    path('get_stock/', get_stock),
]
