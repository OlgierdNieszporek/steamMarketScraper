import threading

from project import app, sched
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart
from project.pageScraper.scheduler import *

if __name__ == '__main__':
    print('guwno')
    app.run(use_reloader=False)
