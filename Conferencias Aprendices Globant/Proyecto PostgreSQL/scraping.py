
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

    return items

def get_info_items(item):
    info_items = {}
    info_items["Item name"] = item.find('a', class_='title').text
    info_items["Caterogy"] = item.find('div', class_='category').text
    info_items["Price"] = item.find('div', class_='price').text
    info_items["Price before"] = item.find('del', class_='d-inline-block')
    info_items["Price before"] = info_items["Price before"].text if info_items["Price before"] else ""

    return info_items

if __name__  == "__main__":
    BASE_URL = 'https://todotintasysuministros.com/celulares-y-tablets?'
    page_site = 4
    items = get_html_info(BASE_URL,page_site)

    list_info_items = []
    for item in items:
        info_items = get_info_items(item)
        list_info_items.append(info_items)

    data_json = r"C:\Users\SENA\Documents\ADSO2717785MariaPaula\items_tintas.json"

    with open(data_json, "w") as outfile:
        json.dump(list_info_items,outfile,indent=4)



