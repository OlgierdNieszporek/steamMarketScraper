import datetime


def getCurrentDate():
    current_date = datetime.date.today()
    return current_date


def getCurrentDateMinusTwoWeeks():
    date = datetime.datetime.now() - datetime.timedelta(days=14)
    return date
