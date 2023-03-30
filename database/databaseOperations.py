from pageScraper import scrapePage
from .establishConnection import *


def executeQuery(sql):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()


def executeQueryReturn(sql):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    result = cursor.fetchall()[0][0]
    connection.close()
    return result

def findMaxId():
    if executeQueryReturn('SELECT Count(*) from market') == 0:
        return 0
    else:
        return executeQueryReturn('SELECT id FROM market ORDER BY id DESC LIMIT 1')

def loadScrapedBuildSqlCommand(dictionary):
    current_max = findMaxId()
    sqlCommand = 'INSERT INTO market VALUES '
    i = 0
    for key in dictionary:
        i += 1
        current_max += 1
        if i == len(dictionary):
            sqlCommand += f"('{current_max}', '{key}', '{dictionary[key]}')\n"
        else:
            sqlCommand += f"('{current_max}', '{key}', '{dictionary[key]}'),\n"
    return sqlCommand


def loadScrapeToDatabase():
    dictionary = scrapePage.scrapeStockMarket()
    executeQuery(loadScrapedBuildSqlCommand(dictionary))
    print("Data loaded successfully")
