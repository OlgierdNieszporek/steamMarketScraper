from .establishConnection import *
from ..models.ProductModel import ProductModel
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
    sqlCommand = 'DELETE FROM market WHERE date ="' + str(systemOperations.getCurrentDateMinusTwoWeeks()) + '"'
    return sqlCommand


def getAllProducts():
    products = []
    newestDate = getValuesFromDatabase('SELECT date FROM market ORDER BY date DESC LIMIT 1')[0]
    id = getValuesFromDatabase('SELECT id FROM market WHERE date ="' + str(newestDate) + '"')
    names = getValuesFromDatabase('SELECT product FROM market WHERE date ="' + str(newestDate) + '"')
    values = getValuesFromDatabase('SELECT price FROM market WHERE date ="' + str(newestDate) + '"')
    date = getValuesFromDatabase('SELECT date FROM market WHERE date ="' + str(newestDate) + '"')
    for i in id:
        newValue = ProductModel(id[i - 1], names[i - 1], values[i - 1], date[i - 1])
        products.append(newValue)
    return products


def getProductByName(productName):
    #(self,id, productName, productPrice, date):
    product = ProductModel(
        getValuesFromDatabase('SELECT id FROM market WHERE product ="' + productName + '"')[0],
        getValuesFromDatabase('SELECT product FROM market WHERE product ="' + productName + '"')[0],
        getValuesFromDatabase('SELECT price FROM market WHERE product ="' + productName + '"')[0],
        getValuesFromDatabase('SELECT date FROM market WHERE product ="' + productName + '"')[0]
    )
    # product.date = getValuesFromDatabase('SELECT date FROM market WHERE product ="' + productName + '"')[0]
    # product.id = getValuesFromDatabase('SELECT id FROM market WHERE product ="' + productName + '"')[0]
    # product.name = getValuesFromDatabase('SELECT product FROM market WHERE product ="' + productName + '"')[0]
    # product.value = getValuesFromDatabase('SELECT price FROM market WHERE product ="' + productName + '"')[0]
    # product.date = getValuesFromDatabase('SELECT date FROM market WHERE product ="' + productName + '"')[0]
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
    # product.date = getValuesFromDatabase('SELECT date FROM market WHERE id ="' + str(productID) + '"')[0]
    # product.id = getValuesFromDatabase('SELECT id FROM market WHERE id ="' + str(productID) + '"')[0]
    # product.name = getValuesFromDatabase('SELECT product FROM market WHERE id ="' + str(productID) + '"')[0]
    # product.value = getValuesFromDatabase('SELECT price FROM market WHERE id ="' + str(productID) + '"')[0]
    # product.date = getValuesFromDatabase('SELECT date FROM market WHERE id ="' + str(productID) + '"')[0]
    return product
