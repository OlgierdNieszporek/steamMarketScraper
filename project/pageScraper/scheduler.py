import atexit

import schedule
import time

from apscheduler.schedulers.background import BackgroundScheduler

from project.Database.databaseOperations import *
iterator = 0

def job():
    nonlocal iterator
    if iterator%2!=0 :
        iterator +=1
        return "Dupa cyce"
    else:
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