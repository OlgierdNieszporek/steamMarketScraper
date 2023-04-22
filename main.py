import threading

from project import app, scheduler
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart
from project.pageScraper.scheduler import *

if __name__ == '__main__':
    scheduler.add_job(id='Scheduled job', func=schedulerJob, trigger='interval', seconds=5)
    scheduler.start()
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
