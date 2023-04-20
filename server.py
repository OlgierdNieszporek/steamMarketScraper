import threading

from project import app
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart
from project.pageScraper.multiThreading import *

if __name__ == '__main__':
    threading.Thread(target=worker, daemon=False).start()
    threading.Thread(target=master(), daemon=False).start()
    #app.run(host="localhost", port=8000, debug=True, use_reloader=False)

