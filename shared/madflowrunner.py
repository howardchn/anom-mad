import shared.data_loader as data_loader
from algo.mad import (mad_based_outlier, get_mad_outlier)
from stopwatch import Stopwatch

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def data_it(raw_data, block_size = 20):
    for i in range(len(raw_data) - block_size):
        eval_data = raw_data[i:i + block_size]
        yield eval_data


def run_mad_anom_detection_flow(file_path):
    data = data_loader.load_data(file_path)
    data_flow = data_it(data, 200)

    try:
        for data_block in data_flow:
            outerliner = get_mad_outlier(data_block)
    except StopIteration:
        pass