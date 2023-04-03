import os

import datetime
import pandas as pd
from project import app
from flask import render_template, redirect, url_for, request



CHART_FOLDER = os.path.join('static', 'productCharts')
app.config['CHART_FOLDER'] = CHART_FOLDER
@app.route('/')
@app.route('/<product_name>')
def show_index(product_name):
    print(product_name)
    full_filename = os.path.join(app.config['CHART_FOLDER'], 'Wykres_'+product_name+'.png')
    print(full_filename)
    #
    return render_template("ProductPage.html.j2",  product_chart_image=full_filename, product_name=product_name,utc_dt=datetime.datetime.utcnow())