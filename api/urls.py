from scraper.views import get_stock,get_meta_of_stock
from django.urls import path, include

urlpatterns = [
    path('get_stock/', get_stock),
    path('get_meta_of_stock/', get_meta_of_stock),
]
