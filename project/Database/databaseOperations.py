from .establishConnection import *
from ..pageScraper import scrapePage
from project.pageScraper import systemOperations


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
    result = cursor.fetchall()
    connection.close()
    return result


def getValuesFromDatabase(sql):
    to_return = []
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    result = cursor.fetchall()
    for res in result:
        to_return.append(res[0])
    connection.close()
    return to_return


def findMaxId():
    if executeQueryReturn('SELECT Count(*) from market')[0][0] == 0:
        return 0
    else:
        return executeQueryReturn('SELECT id FROM market ORDER BY id DESC LIMIT 1')[0][0]


def loadScrapedBuildSqlCommand(dictionary):
    current_max = findMaxId()
    sqlCommand = 'INSERT INTO market VALUES '
    i = 0
    for key in dictionary:
        i += 1
        current_max += 1
        if i == len(dictionary):
            sqlCommand += f"('{current_max}', '{key}', '{dictionary[key]}', '{systemOperations.getCurrentDate()}')\n"
        else:
            sqlCommand += f"('{current_max}', '{key}', '{dictionary[key]}', '{systemOperations.getCurrentDate()}'),\n"
    return sqlCommand

def removeDataFromDatabase():
    sqlCommand = 'DELETE FROM market WHERE date ="' + str(systemOperations.getCurrentDateMinusTwoWeeks()) + '"'
    return sqlCommand

def loadScrapeToDatabase():
    dictionary = scrapePage.scrapeStockMarket()
    executeQuery(loadScrapedBuildSqlCommand(dictionary))
    print("Data loaded successfully")
