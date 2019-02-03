import numpy as np

def percentile_based_outlier(data, threshold=95):
    diff = (100 - threshold) / 2.0
    minval, maxval = np.percentile(data, [diff, 100 - diff])

    isAnom = (data < minval) | (data > maxval)
    return isAnom, minval, maxval

def get_percentile_based_outlier(data, threshold=95):
    diff = (100 - threshold) / 2.0
    minval, maxval = np.percentile(data, [diff, 100 - diff])
    med = np.median([minval, maxval])
    last_index = len(data) - 1

    isAnom = (data < minval) | (data > maxval)
    raw = data[-1]
    ts = data.index[-1]

    return maxval, minval, raw, ts, med