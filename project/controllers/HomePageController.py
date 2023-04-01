
import os
import pandas as pd
from project import app
from flask import render_template, redirect, url_for

#route index
@app.route('/')
def index():
    data = {
        "title": "KUPSKO",
        "body": "KUPA KUPA KUPA"
    }
    return render_template('HomePage.html.j2', data = data)



@app.route('/')
@app.route('/Table')
def table():
    data_dic = {
        'id': [100, 101, 102],
        'color': ['red', 'blue', 'red']}
    columns = ['id', 'color']
    index = ['a', 'b', 'c']

    df = pd.DataFrame(data_dic, columns=columns, index=index)
    table2 = df.to_html(index=False)

    return render_template("ProductPage.html.j2", table=table2)



CHART_FOLDER = os.path.join('static', 'productCharts')
app.config['CHART_FOLDER'] = CHART_FOLDER
@app.route('/')
@app.route('/image')
def show_index():
    full_filename = os.path.join(app.config['CHART_FOLDER'], 'Wykres.png')
    return render_template("ImagePage.html.j2", user_image = full_filename)