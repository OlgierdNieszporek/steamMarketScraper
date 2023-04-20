import threading

from project import app
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart
from project.pageScraper.multiThreading import *


if __name__ == '__main__':
    #runApp()
    app.run(host='0.0.0.0', debug=True, use_reloader=False, threaded=True)
    # app.run(host="localhost", port=8000, debug=True, use_reloader=False)