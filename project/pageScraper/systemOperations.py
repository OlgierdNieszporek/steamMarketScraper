import datetime


def getCurrentDate():
    current_date = datetime.date.today() + datetime.timedelta()
    return current_date


def getCurrentDateMinusWeek():
    date = datetime.datetime.now() - datetime.timedelta(7)
    print(date)
    return date
