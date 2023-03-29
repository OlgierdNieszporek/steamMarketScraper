from time import sleep

from bs4 import BeautifulSoup
import requests
import strings


def scrapeSteamMarket():
    iterateThroughWholeMarket()

def createCasesList(casesnames, casesList):
    for casename in casesnames:
        casesList.append(casename.text)
    return casesList


def createPricesList(prices, pricesList):
    for price in prices:
        pricesList.append(price.text)
    return pricesList


# def createProductsAndPricesMap(casesnames, prices):
#     caseWithPricesMap = {case: price for case, price in zip(createCasesList(casesnames), createPricesList(prices))}
#     return caseWithPricesMap


def iterateThroughWholeMarket():
    product_list, price_list = [], []
    url = strings.url
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    product_names = soup.findAll("td", attrs={"class": "colWalor textNowrap"})
    product_list = [name.text.strip() for name in product_names]
    prices = soup.findAll("td", attrs={"class": "colKurs"})
    price_list = createPricesList(prices, price_list)
    print(url)
    print(product_list)
    print(price_list)