import os
import pandas as pd
from project import app
from flask import render_template, redirect, url_for, request
from project.Database.databaseOperations import *

#to jest mock danych do testow
newestDate = getValuesFromDatabase('SELECT date FROM market ORDER BY date DESC LIMIT 1')[0]
id = getValuesFromDatabase('SELECT id FROM market WHERE date ="' + str(newestDate) + '"')
names = getValuesFromDatabase('SELECT product FROM market WHERE date ="' + str(newestDate) + '"')
values = getValuesFromDatabase('SELECT price FROM market WHERE date ="' + str(newestDate) + '"')
date = getValuesFromDatabase('SELECT date FROM market WHERE date ="' + str(newestDate) + '"')

# route index
@app.route('/')
def index():
    df = pd.DataFrame({
        'No.': [],
        'Name': [],
        'Value': [],
        'Date': []})
    for i in range(0, len(id)):
        df.loc[id[i]] = [i+1, names[i], values[i], date[i]]

    df['Name'] = df['Name'].apply(lambda x: f'<a href="../{x}">{x}</a>')
    table = df.to_html(index=False, escape=False)

    return render_template("HomePage.html.j2", table=table)
