import os

from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
from project import app
import io
import base64
import pandas as pd
from project import app
from flask import render_template, redirect, url_for


from flask import Flask, send_file

####
#Do OGARNIECIA JAK W FLASKU WYSWEITLIC PNG
###
# przygotowanie danych


#@app.get('/aaaImage')
def show_image():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    # wykres
    fig = Figure()
    ax = fig.subplots()
    ax.plot(x, y)
    # zapis do pliku png
    png_output = io.BytesIO()
    FigureCanvas(fig).print_png(png_output)
    # kodowanie do base64
    png_output = base64.b64encode(png_output.getvalue()).decode('utf-8')

    # wyświetlenie w HTML
    html = f'<img src="data:image/png;base64,{png_output}">'
    png_output.save(os.path.join(app.root_path, 'static', 'customlogos', 'wykres.png'))
    filename = os.path.join(app.root_path, 'static', 'customlogos', 'wykres.png')
    # send_file(filename, mimetype='image/png')
    return html