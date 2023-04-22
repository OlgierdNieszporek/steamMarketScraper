from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_apscheduler import APScheduler

from project.pageScraper.scheduler import *


app = Flask("project")
scheduler = APScheduler()

from project.controllers import *