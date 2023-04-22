from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_apscheduler import APScheduler

from project.pageScraper.scheduler import *

print('chuj')
app = Flask(__name__)
print('aaaa')
sched = APScheduler()
from project.controllers import *

#runScheduler()