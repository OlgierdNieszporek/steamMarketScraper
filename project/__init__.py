from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from project.pageScraper.scheduler import *
import multiprocessing

sched = BackgroundScheduler(daemon=True)
sched.add_job(job, 'interval', seconds=10)
sched.start()

if not multiprocessing.current_process().name == 'MainProcess':
    sched.shutdown()
app = Flask("project")

from project.controllers import *