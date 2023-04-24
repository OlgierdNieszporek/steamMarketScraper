import os
import pandas as pd
from project import app, runScheduler
from flask import render_template, redirect, url_for, request

from project.Database.databaseOperations import getAllProducts


# route index
@app.route('/')
def index():
    df = pd.DataFrame({
        'No.': [],
        'Name': [],
        'Value': [],
        'ROI': [],
        'Date': []})
    products = getAllProducts()
    # print(products.count())
    for product in products:
        df.loc[product.id] = [product.id, product.productName, product.productPrice, product.ROI, product.date]

    df['Name'] = df['Name'].apply(lambda x: f'<a href="../{x}">{x}</a>')
    table = df.to_html(index=False, escape=False)


    return render_template("HomePage.html.j2", table=table)

runScheduler()
