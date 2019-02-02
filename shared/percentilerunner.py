import shared.data_loader
from algo.percentile import percentile_based_outlier
from stopwatch import Stopwatch

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def run_percentile_detection(file_path):
    data = data_loader.load_data(file_path)
    r = percentile_based_outlier(data)

    min_values = [r[1] for i in range(len(r[0]))]
    max_values = [r[2] for i in range(len(r[0]))]

    plt.plot(data.index, data.values)
    plt.plot(data.index, min_values)
    plt.plot(data.index, max_values)

    for i in range(len(r[0])):
        if r[0].values[i]:
            plt.plot(data.index[i], data.values[i], 'ro')

    plt.show()