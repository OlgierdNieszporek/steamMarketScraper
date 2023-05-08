import threading

from project import app
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart
from project.pageScraper.scheduler import *

if __name__ == '__main__':
    print('jajco')
    app.run(use_reloader=False)
