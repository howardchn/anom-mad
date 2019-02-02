from scipy.stats import norm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data_loader
from algo.percentile import percentile_based_outlier
from algo.mad import (mad_based_outlier, get_mad_outlier)

SAMPLE_FILE_PATH = './data/santaba-demo4.csv'

def run_mad_anom_detection():
    data = data_loader.load_data(SAMPLE_FILE_PATH)
    r = mad_based_outlier(data)

    r1 = get_mad_outlier(data)
    max_values = [r1[0][0] for i in range(len(r))]
    min_values = [r1[1][0] for i in range(len(r))]
    plt.plot(data.index, min_values)
    plt.plot(data.index, max_values)
    
    plt.plot(data.index, data.values)
    for i in range(len(r)):
        if r[i]:
            plt.plot(data.index[i], data.values[i], 'ro')

    plt.show()

def run_percentile_detection():
    data = data_loader.load_data(SAMPLE_FILE_PATH)
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

import sys
import getopt
def main():
    algo_type = 'mad'

    opts, args = getopt.getopt(sys.argv[1:], 'a:', ['algo'])
    for opt_name, opt_value in opts:
        if opt_name in ('-a', '--algo'):
            algo_type = opt_value

    if algo_type == 'mad':
        run_mad_anom_detection()
    else:
        run_percentile_detection()


def main1():
    nums = np.asarray([1,4,23,60,80])
    # meds = np.median(np.asarray(nums), axis=0)
    nums1 = np.sum(nums ** 2, axis=-1)
    nums1 = np.sqrt(nums1)
    print(nums1)

main()
