from bs4 import BeautifulSoup
import requests

def get_all_stock_urls():
    try:
        page = 'https://stocks.zerodha.com/'
        soup = BeautifulSoup(requests.get(page).text, 'html.parser')
        print(soup.prettify())
    except Exception as e:
        print(e)