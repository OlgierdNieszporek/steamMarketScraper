from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from project.pageScraper.scheduler import *

runScheduler()
app = Flask("project")


from project.controllers import *