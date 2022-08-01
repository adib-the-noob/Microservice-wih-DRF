from bs4 import BeautifulSoup
import requests
from .models import Stocks

def get_all_stock_urls():
    try:
        page = 'https://stocks.zerodha.com/'
        soup = BeautifulSoup(requests.get(page).text, 'html.parser')
        print(soup.prettify())
        for ul in soup.find_all('div',class_="index-page"):
            for li in ul.findAll('li'):
                anchor_tag = li.find('a')
                anchor_tag.get('href')
                Stocks.objects.get_or_create(
                    stock_url = anchor_tag['href'],
                    stock_name = anchor_tag.text,
                )
    except Exception as e:
        print(e)