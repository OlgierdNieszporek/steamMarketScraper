from pageScraper import scrapePage
from .establishConnection import *


def loadScrapedBuildSqlCommand(dictionary):
    sqlCommand = 'INSERT INTO market VALUES '
    i = 0
    for key in dictionary:
        i += 1
        if i == len(dictionary):
            sqlCommand += f"('{i}', '{key}', '{dictionary[key]}')\n"
        else:
            sqlCommand += f"('{i}', '{key}', '{dictionary[key]}'),\n"
    return sqlCommand


def loadScrapeToDatabase():
    connection = connect()
    cursor, dictionary = connection.cursor(), scrapePage.scrapeStockMarket()
    cursor.execute(loadScrapedBuildSqlCommand(dictionary))
    connection.commit()
    print("Data loaded successfully")
