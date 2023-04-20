import multiprocessing

import schedule
import time

from apscheduler.schedulers.background import BackgroundScheduler

from project.Database.databaseOperations import *

def job():
    #screapeData
    #loadScrapeToDatabase()

    #deleteFromDBIfOlderThanTwoWeeks
    #removeDataFromDatabase()

    #generateNewCharts()

    #updateFront()
    print("Done scheduled tasks")


def runScheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(job, 'interval', seconds=10)
    sched.start()

    if not multiprocessing.current_process().name == 'MainProcess':
        sched.shutdown()

    # sched = BackgroundScheduler(daemon=True)
    # sched.add_job(job, 'interval', seconds=5)
    # sched.start()