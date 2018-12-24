import numpy as np

def percentile_based_outlier(data, threshold=95):
    diff = (100 - threshold) / 2.0
    minval, maxval = np.percentile(data, [diff, 100 - diff])

    isAnom = (data < minval) | (data > maxval)
    return isAnom, minval, maxval