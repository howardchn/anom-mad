import shared.data_loader as data_loader
from algo.mad import (mad_based_outlier, get_mad_outlier)
from stopwatch import Stopwatch
from pandas import DataFrame

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def data_it(raw_data, block_size = 20):
    for i in range(len(raw_data) - block_size):
        eval_data = raw_data[i : i + block_size]
        yield eval_data


def run_mad_anom_detection_flow(file_path, block_size = 30):
    data = data_loader.load_data(file_path)
    data_flow = data_it(data, block_size)

    sw = Stopwatch()
    sw.start()
    columns = ['max', 'min', 'raw', 'ts']
    df = []
    try:
        for data_block in data_flow:
            outerliner = get_mad_outlier(data_block)
            df.append(outerliner)
            
    except StopIteration as ex:
        print(ex)
    sw.stop()
    print(sw.duration)

    df = DataFrame(df, columns = columns)
    plt.fill_between(df['ts'].values, df['max'].values, df['min'].values, color='lightgray')
    plt.plot(df['ts'].values, df['raw'].values)

    for i in range(len(df)):
        raw_row = df.values[i]
        if raw_row[2] < raw_row[1] or raw_row[2] > raw_row[0]:
            plt.plot(raw_row[3], raw_row[2], 'ro')

    plt.show()