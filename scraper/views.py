from django.shortcuts import render
from django.http import JsonResponse
from .helpers import get_all_stock_urls,get_stock_price
# Create your views here.


def get_meta_of_stock(request):
    get_stock_price()
    return JsonResponse({'status': 200})



def get_stock(request):
    get_all_stock_urls()
    return JsonResponse({'status': 200})
