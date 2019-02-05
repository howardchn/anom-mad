import shared.data_loader as data_loader
from algo.mad import (mad_based_outlier, get_mad_outlier)
from stopwatch import Stopwatch

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def run_mad_anom_detection(file_path):
    data = data_loader.load_data(file_path)
    r = mad_based_outlier(data)

    sw = Stopwatch()
    sw.start()
    r1 = get_mad_outlier(data)
    sw.stop()
    print(sw.duration)

    if r1[0] is not None:
        max_values = [r1[0] for i in range(len(r))]
        plt.plot(data.index, max_values)
    
    if r1[1] is not None:
        min_values = [r1[1] for i in range(len(r))]
        plt.plot(data.index, min_values)
    
    plt.plot(data.index, data.values)
    for i in range(len(r)):
        if r[i]:
            plt.plot(data.index[i], data.values[i], 'ro')

    plt.show()