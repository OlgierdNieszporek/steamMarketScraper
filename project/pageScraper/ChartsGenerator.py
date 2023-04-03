import os
import matplotlib.pyplot as plt

from project import app




def generateChart(product_name, xAxis , yAxis):
    # mock danych
    xAxis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    yAxis = [5, 7, 8, 1, 4, 9, 6, 3, 5, 2, 1, 8]

    x_axis =xAxis
    y_axis = yAxis

    plt.plot(x_axis, y_axis)
    plt.title(product_name)
    plt.xlabel('x')
    plt.ylabel('y')

    full_filename = os.path.join(app.config['CHART_FOLDER'], 'project\Wykres_'+product_name+'.png')
    print(full_filename)
    plt.savefig('output.jpg')
    plt.show()

