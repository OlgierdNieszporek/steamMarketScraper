import threading

from project import app#, scheduler
from project.Database.databaseOperations import loadScrapeToDatabase
# from project.pageScraper.ChartsGenerator import generateChart
from project.pageScraper.scheduler import *

if __name__ == '__main__':
    #scheduler.add_job(id='Scheduled job', func=schedulerJob, trigger='interval', seconds=5)
    #scheduler.start()

    from waitress import serve

    serve(app, host="0.0.0.0", port=8080, debug=False, use_reloader=False)
    #runScheduler()
    #app.run(debug=False, use_reloader=False)
