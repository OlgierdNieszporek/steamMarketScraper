from bs4 import BeautifulSoup
import requests
import strings

def createDict(names, prices):
    dictionary = {}
    for i in range(0, len(names)):
        dictionary[names[i]] = prices[i]
    return dictionary


def printDict(dict):
    for key, value in dict.items():
        print(key, ': ', value)


def scrapeStockMarket():
    url = strings.url
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    product_names = soup.findAll("td", attrs={"class": "colWalor textNowrap"})
    product_list = [name.text.strip() for name in product_names]

    prices = soup.findAll("td", attrs={"class": "colKurs"})
    prices_list = [price.text.strip() for price in prices]

    dictionary = createDict(product_list, prices_list)

    printDict(dictionary)