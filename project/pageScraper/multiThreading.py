import threading
import time
from project.pageScraper.scheduler import *
from project import app


def master():
    while True:
        # app.run(host="localhost", port=8000, debug=True, use_reloader=False)
        app.run(host='0.0.0.0', debug=True, use_reloader=False)


def worker():
    while True:
        runScheduler()


def runApp():
    threading.Thread(target=worker, daemon=False).start()
    threading.Thread(target=master(), daemon=False).start()
