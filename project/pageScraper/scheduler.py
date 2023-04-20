import schedule
import time
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
    schedule.every().day.at("18:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)