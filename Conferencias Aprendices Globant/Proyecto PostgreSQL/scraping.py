#import_librerias
from bs4 import BeautifulSoup
import requests
import json 

def get_html_info(base_url,pages_site):

    items = []

    for n in range(1, pages_site):

        url = f"{base_url}page={n}"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        items_found = soup.find_all('div', class_= 'infor')
        items.extend(items_found)