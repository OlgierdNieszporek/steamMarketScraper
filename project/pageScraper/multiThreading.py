import threading
import time
from project.pageScraper.scheduler import *
from project import app

def master():
    while True:
        #app.run(host="localhost", port=8000, debug=True, use_reloader=False)
        app.run(debug=True, use_reloader=False)

def worker():
    while True:
        runScheduler()

