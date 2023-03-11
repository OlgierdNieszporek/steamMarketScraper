from time import sleep

from bs4 import BeautifulSoup
import requests
import strings
import re


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


def createProductsAndPricesMap(casesnames, prices):
    caseWithPricesMap = {case: price for case, price in zip(createCasesList(casesnames), createPricesList(prices))}
    return caseWithPricesMap


def iterateThroughWholeMarket():
    casesList = []
    pricesList = []
    for i in range(37):
        url = strings.urlP1 + str(i + 1) + strings.urlP2
        pageToScrape = requests.get(url)
        soup = BeautifulSoup(pageToScrape.text, "html.parser")
        casesnames = soup.findAll("span", attrs={"class": "market_listing_item_name"})
        prices = soup.findAll("span", attrs={"class": "normal_price", "data-currency": "1"})
        casesList = createCasesList(casesnames, casesList)
        pricesList = createPricesList(prices, pricesList)
        print(url)
        print(casesList)
        sleep(10)
    createProductsAndPricesMap(casesList, pricesList)

