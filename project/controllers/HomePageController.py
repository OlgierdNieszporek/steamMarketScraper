
import os
import pandas as pd
from project import app
from flask import render_template, redirect, url_for, request
from project.Database.databaseOperations import *


#to jest mock danych do testow
id = getValuesFromDatabase('SELECT id FROM market')
names = getValuesFromDatabase('SELECT product FROM market')
values = getValuesFromDatabase('SELECT price FROM market')

#route index
@app.route('/')
def index():
    df = pd.DataFrame({
        'Id': [],
        'Name': [],
        'Value': []})

    for i in range(0, len(id)):
        df.loc[id[i]] = [id[i], names[i], values[i]]

    df['Name'] = df['Name'].apply(lambda x: f'<a href="../{x}">{x}</a>')
    table = df.to_html(index=False, escape=False)

    return render_template("HomePage.html.j2", table=table)



