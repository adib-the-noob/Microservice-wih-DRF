from bs4 import BeautifulSoup
import requests

def get_all_stock_urls():
    try:
        page = 'https://stocks.zerodha.com/'
        soup = BeautifulSoup(requests.get(page).text, 'html.parser')
        print(soup.prettify())
        for ul in soup.find_all('div',class_="index-page"):
            for li in ul.find_all('li'):
                anchor_tag = li.find('a')
                print(anchor_tag['href'])
                print(anchor_tag.text)
    except Exception as e:
        print(e)