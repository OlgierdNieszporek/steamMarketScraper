import os
from typing import re

import pandas as pd
from project import app
from flask import render_template, redirect, url_for, request

from project.Database.databaseOperations import getProductByName, getProductHistory

CHART_FOLDER = os.path.join('static', 'productCharts')
app.config['CHART_FOLDER'] = CHART_FOLDER


@app.route('/')
@app.route('/<product_name>')
def show_index(product_name):
    df = pd.DataFrame({
        'Date': [],
        'Price': []})

    # product = getProductByName(product_name)
    productHistory = getProductHistory(product_name)
    # productHistory = [['3.5500', '3.5500', '3.5500', '3.5500', '3.5500', '3.3400', '3.5500'], ['2023-04-19', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25']]

    k1 = float(productHistory[0][6])
    k0 = float(productHistory[0][5])

    roi = round(((k1 - k0) / k0), 2)

    for i in range(0, len(productHistory[1])):
        df.loc[i] = [(productHistory[1])[i], (productHistory[0])[i]]

    dfTransposed = df.set_index(['Date', 'Price']).T
    table = dfTransposed.to_html(index=False, escape=False)

    return render_template("ProductPage.html.j2",
                           product_name=product_name,
                           product_price=productHistory[0][6],
                           product_roi=roi,
                           table=table)  # , price = product.productPrice)
