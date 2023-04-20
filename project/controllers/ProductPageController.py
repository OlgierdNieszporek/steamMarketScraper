import os
from project import app
from flask import render_template, redirect, url_for, request

from project.Database.databaseOperations import getProductByName


CHART_FOLDER = os.path.join('static', 'productCharts')
app.config['CHART_FOLDER'] = CHART_FOLDER


# @app.route('/')
# @app.route('/<product_name>')
# def show_index(product_name):
#     product = getProductByName(product_name)
#     #full_filename = os.path.join(app.config['CHART_FOLDER'], 'Wykres_' + product_name + '.png')
#     print(CHART_FOLDER)
#     full_filename = os.path.join(app.config['CHART_FOLDER'], 'Wykres_' + 'basic' + '.png')
#
#     #
#     return render_template("ProductPage.html.j2",
#                            product_chart_image=full_filename,
#                            product_name=product.productName,
#                            product_price=product.productPrice,
#                            utc_dt=product.date
#                            )
