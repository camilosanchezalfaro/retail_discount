import requests
from bs4 import BeautifulSoup

def get_discounts(discount_percentage):
    results = []
    
    # Falabella scraping
    falabella_url = f'https://www.falabella.com/falabella-cl/search?Ntt={discount_percentage}%25+descuento'
    falabella_response = requests.get(falabella_url)
    if falabella_response.status_code == 200:
        soup = BeautifulSoup(falabella_response.text, 'html.parser')
        for product in soup.select('.product-card'):
            title = product.select_one('.pod-subTitle').text
            price = product.select_one('.price-0').text
            results.append({"title": title, "price": price, "source": "Falabella"})

    # Paris scraping
    paris_url = f'https://www.paris.cl/buscar/?q={discount_percentage}%25+descuento'
    paris_response = requests.get(paris_url)
    if paris_response.status_code == 200:
        soup = BeautifulSoup(paris_response.text, 'html.parser')
        for product in soup.select('.product-card'):
            title = product.select_one('.product-name').text
            price = product.select_one('.product-price').text
            results.append({"title": title, "price": price, "source": "Paris"})

    # Ripley scraping
    ripley_url = f'https://simple.ripley.cl/search?term={discount_percentage}%25+descuento'
    ripley_response = requests.get(ripley_url)
    if ripley_response.status_code == 200:
        soup = BeautifulSoup(ripley_response.text, 'html.parser')
        for product in soup.select('.catalog-product'):
            title = product.select_one('.catalog-product-name').text
            price = product.select_one('.catalog-product-price').text
            results.append({"title": title, "price": price, "source": "Ripley"})

    return results
