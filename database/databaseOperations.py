from pageScraper import scrapePage
from .establishConnection import *


def executeQuery(sql):
    connection = connect()
    cursor, dictionary = connection.cursor(), scrapePage.scrapeStockMarket()
    cursor.execute(sql)
    connection.commit()
    result = cursor.fetchall()[0][0]
    return result

def findMaxId():
    if executeQuery('SELECT Count(*) from market') == 0:
        return 0
    else:
        return executeQuery('SELECT id FROM market ORDER BY id DESC LIMIT 1')

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
    connection = connect()
    cursor, dictionary = connection.cursor(), scrapePage.scrapeStockMarket()
    cursor.execute(loadScrapedBuildSqlCommand(dictionary))
    connection.commit()
    print("Data loaded successfully")
    connection.close()
