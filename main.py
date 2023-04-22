import threading

from project import app, sched
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart
from project.pageScraper.scheduler import *

if __name__ == '__main__':
    sched.add_job(id='Scheduled job', func=schedulerJob, trigger='interval', seconds=5)
    sched.start()
    print('guwno')
    app.run(use_reloader=False)
