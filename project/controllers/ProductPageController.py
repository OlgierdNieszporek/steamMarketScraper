import os
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

    #product = getProductByName(product_name)
    productHistory = getProductHistory(product_name)
    #productHistory = [['3.5500', '3.5500', '3.5500', '3.5500', '3.5500', '3.3400', '3.5500'], ['2023-04-19', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25']]


    for i in range(0, len(productHistory[1])):
        df.loc[i] = [(productHistory[1])[i], (productHistory[0])[i]]

    table = df.to_html(index=False, escape=False)
    #df.transpose(table)
    #return render_template("ProductPage.html.j2", table = table, name = product_name, price = product.productPrice)
    return render_template("ProductPage.html.j2", table = table)
    # product = getProductByName(product_name)
    # #full_filename = os.path.join(app.config['CHART_FOLDER'], 'Wykres_' + product_name + '.png')
    # print(CHART_FOLDER)
    # full_filename = os.path.join(app.config['CHART_FOLDER'], 'Wykres_' + 'basic' + '.png')
    #
    # return render_template("ProductPage.html.j2",
    #                       # product_chart_image=full_filename,
    #                        product_name=product.productName,
    #                        product_price=product.productPrice,
    #                        utc_dt=product.date
    #                        )
