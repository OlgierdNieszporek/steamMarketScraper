from pageScraper import scrapePage
from database import establishConnection, databaseOperations

if __name__ == '__main__':
    databaseOperations.loadScrapeToDatabase()

