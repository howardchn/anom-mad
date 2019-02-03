import shared.data_loader as data_loader
from algo.percentile import (percentile_based_outlier, get_percentile_based_outlier)
from stopwatch import Stopwatch
from pandas import DataFrame

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

def run_percentile_detection_flow(file_path, threshold = 97, block_size = 120):
    data = data_loader.load_data(file_path)
    data_flow = data_loader.data_it(data, block_size)
    df = []
    try:
        for data_block in data_flow:
            outerliner = get_percentile_based_outlier(data_block, threshold)
            df.append(outerliner)
            
    except StopIteration as ex:
        print(ex)

    columns = ['max', 'min', 'raw', 'ts', 'med']
    df = DataFrame(df, columns = columns)
    plt.fill_between(df['ts'].values, df['max'].values, df['min'].values, color='lightgray')
    plt.plot(df['ts'].values, df['raw'].values)
    plt.plot(df['ts'].values, df['med'].values)

    for i in range(len(df)):
        raw_row = df.values[i]
        if raw_row[2] < raw_row[1] or raw_row[2] > raw_row[0]:
            plt.plot(raw_row[3], raw_row[2], 'ro')

    plt.show()