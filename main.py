import threading

from project import app
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, use_reloader=False)