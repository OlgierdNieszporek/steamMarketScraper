#Project Flask MVC


__author__ = "indhifarhandika"
__version__ = "1"
__email__ = "indhifarhandika@gmail.com"

from project import app
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True, use_reloader=False)

