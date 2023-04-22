from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_apscheduler import APScheduler

from project.pageScraper.scheduler import *

print('chuj')
app = Flask(__name__)
print('aaaa')
sched = APScheduler()
sched.add_job(id='Scheduled job', func=schedulerJob, trigger='interval', seconds=5)
sched.start()
from project.controllers import *

#runScheduler()