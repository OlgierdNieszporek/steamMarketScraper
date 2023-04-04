import os
import sqlite3

dbPath = os.path.join('project', 'Database', 'Chinook.db')

def connect():
    print(dbPath)
    connection = sqlite3.connect(dbPath)
    return connection
