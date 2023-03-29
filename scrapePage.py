from time import sleep

from bs4 import BeautifulSoup
import requests
import strings

def createProductsList(products_names, products_list):
    for case_name in products_names:
        products_list.append(case_name.text)
    return products_list


def createPricesList(prices, prices_list):
    for price in prices:
        prices_list.append(price.text)
    return prices_list


def scrapeStockMarket():
    product_list, price_list = [], []
    url = strings.url
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    product_names = soup.findAll("td", attrs={"class": strings.product_name_string})
    prices = soup.findAll("td", attrs={"class": strings.prices_string})
    product_list = [name.text.strip() for name in product_names]
    price_list = createPricesList(prices, price_list)
    print(product_list)
    print(price_list)
    return product_list, price_list
