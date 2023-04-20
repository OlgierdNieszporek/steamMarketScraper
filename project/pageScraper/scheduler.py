import atexit

import schedule
import time

from apscheduler.schedulers.background import BackgroundScheduler

from project.Database.databaseOperations import *

def job():
    #screapeData
    #loadScrapeToDatabase()

    #deleteFromDBIfOlderThanTwoWeeks
    #removeDataFromDatabase()

    #generateNewCharts

    #updateFront
    print("Done scheduled tasks")


def runScheduler():
    sched = BackgroundScheduler(daemon=False)
    sched.add_job(job, 'interval', seconds=5)
    sched.start()
    atexit.register(lambda: sched.shutdown())