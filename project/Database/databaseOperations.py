from .establishConnection import *
from ..models.ProductModel import ProductModel
from ..pageScraper import scrapePage
from project.pageScraper import systemOperations
import re


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


def fetchNewestDateFromDatabase():
    newestDate = getValuesFromDatabase('SELECT date FROM market ORDER BY date DESC LIMIT 1')[0]
    return newestDate


def fetchNewestIds():
    ids = getValuesFromDatabase('SELECT id FROM market WHERE date ="' + str(fetchNewestDateFromDatabase()) + '"')
    return ids


def fetchNames():
    newestDate = fetchNewestDateFromDatabase()
    names = getValuesFromDatabase('SELECT product FROM market WHERE date ="' + str(newestDate) + '"')
    return names


def fetchNewestValues():
    newestDate = fetchNewestDateFromDatabase()
    values = getValuesFromDatabase('SELECT price FROM market WHERE date ="' + str(newestDate) + '"')
    return values


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


def loadScrapeToDatabase():
    dictionary = scrapePage.scrapeStockMarket()
    executeQuery(loadScrapedBuildSqlCommand(dictionary))
    print("Data loaded successfully")


def removeDataFromDatabase():
    sqlCommand = executeQueryReturn(
        'DELETE FROM market WHERE date <="' + str(systemOperations.getCurrentDateMinusWeek()) + '"')
    return sqlCommand


def getAllProducts():
    products = []
    # newestDate = getValuesFromDatabase('SELECT date FROM market ORDER BY date DESC LIMIT 1')[0]
    newestDate = getValuesFromDatabase('SELECT DISTINCT date FROM market ORDER BY date DESC')[0]
    yesterday = getValuesFromDatabase('SELECT DISTINCT date FROM market ORDER BY date DESC')[1]
    id = getValuesFromDatabase('SELECT id FROM market WHERE date ="' + str(newestDate) + '"')
    names = getValuesFromDatabase('SELECT product FROM market WHERE date ="' + str(newestDate) + '"')
    values = getValuesFromDatabase('SELECT price FROM market WHERE date ="' + str(newestDate) + '"')
    values_old = getValuesFromDatabase('SELECT price FROM market WHERE date ="' + str(yesterday) + '"')
    date = getValuesFromDatabase('SELECT date FROM market WHERE date ="' + str(newestDate) + '"')

    for i in range(0, len(id)):
        # tutaj byl blad ze w bazie mi pobieralo jakas z dupy warotsc dlatego wywalamy wszystko co jest przed spacja
        k0 = float(re.sub(r'^\S*\s', '', values_old[i]))
        k1 = float(re.sub(r'^\S*\s', '', values[i]))
        # if  k0 != 0 and k1 != 0 :
        roi = round(((k1 - k0) / k0), 2)

        strRoi = str(roi) + "%"

        newValue = ProductModel(i, names[i], values[i], strRoi, date[i])
        # newValue = ProductModel(id[i], names[i], values[i], date[i]) #indeksowanie zgodne z bazą
        products.append(newValue)
    return products


def getProductByName(productName):
    # (self,id, productName, productPrice, date):
    product = ProductModel(
        getValuesFromDatabase('SELECT id FROM market WHERE product ="' + productName + '"')[0],
        getValuesFromDatabase('SELECT product FROM market WHERE product ="' + productName + '"')[0],
        getValuesFromDatabase('SELECT price FROM market WHERE product ="' + productName + '"')[0],
        getValuesFromDatabase('SELECT date FROM market WHERE product ="' + productName + '"')[0]
    )

    return product


def getProductByID(productID):
    product = ProductModel(
        product=ProductModel(
            getValuesFromDatabase('SELECT id FROM market WHERE id ="' + str(productID) + '"')[0],
            getValuesFromDatabase('SELECT product FROM market WHERE id ="' + str(productID) + '"')[0],
            getValuesFromDatabase('SELECT price FROM market WHERE id ="' + str(productID) + '"')[0],
            getValuesFromDatabase('SELECT date FROM market WHERE id ="' + str(productID) + '"')[0]
        )
    )

    return product
