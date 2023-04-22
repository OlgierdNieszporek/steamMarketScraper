from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from project.pageScraper.scheduler import *

def job():

    #screapeData
    #loadScrapeToDatabase()

    #deleteFromDBIfOlderThanTwoWeeks
    #removeDataFromDatabase()

    #generateNewCharts

    #updateFront
    print("Done scheduled tasks")

print('chuj')
app = Flask(__name__)
sched = BackgroundScheduler(daemon=True)
sched.add_job(job, 'interval', seconds=5)
sched.start()


print('dupa')

from project.controllers import *

#runScheduler()
print('kamieni kupa')