import sqlite3


def connect():
    connection = sqlite3.connect("C:/Users/lksma/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db")
    return connection
