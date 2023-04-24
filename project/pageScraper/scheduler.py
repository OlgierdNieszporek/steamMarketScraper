import atexit
from datetime import datetime

import schedule
import time

from apscheduler.schedulers.background import BackgroundScheduler

from project.Database.databaseOperations import *
def job():

    #screapeData
    loadScrapeToDatabase()
    print("Done loading scrape to database")

    #deleteFromDBIfOlderThanTwoWeeks
    #removeDataFromDatabase()

    #generateNewCharts

    #updateFront
    print("Done scheduled tasks")

def runScheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(job, 'interval', days=1, start_date=datetime.now().replace(hour=23, minute=38, second=55, microsecond=0))
    sched.start()
    #atexit.register(lambda: sched.shutdown())

# def schedulerJob():
#     print("Jebać disa skurwysyna")