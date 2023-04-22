from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from project.pageScraper.scheduler import *

print('chuj')
app = Flask(__name__)
print('dupa')

from project.controllers import *

runScheduler()
print('kamieni kupa')