from django.shortcuts import render
from django.http import JsonResponse
from .helpers import get_all_stock_urls
# Create your views here.

def get_stock(request):
    get_all_stock_urls()
    return JsonResponse({'status': 200})
