from project.Database import databaseOperations

def mapNewestIds():
    newestIds = databaseOperations.fetchNewestIds()
    return newestIds
def mapProductNames():
    productsNames = databaseOperations.fetchNames()
    return productsNames

def mapNewestValues():
    newestValue = databaseOperations.fetchNewestValues()
    return newestValue
def mapNewestDate():
    date = databaseOperations.fetchNewestDateFromDatabase()
    return date
