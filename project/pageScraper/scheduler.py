import schedule
import time


def job():
    #screapeData()
    #deleteFromDBIfOlderThanTwoWeeks()
    #generateNewCharts()
    #updateFront()
    print("Reading time...")


def runScheduler():
    schedule.every().day.at("18:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)