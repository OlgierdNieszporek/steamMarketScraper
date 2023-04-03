
import os
import pandas as pd
from project import app
from flask import render_template, redirect, url_for, request


#to jest mock danych do testow
id = [0, 1]
names = ['basic', 'test']
values = [12, 15.223]

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



