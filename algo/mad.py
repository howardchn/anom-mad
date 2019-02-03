import numpy as np
from scipy.stats import norm

def mad_based_outlier(points, thresh=3.5):
    if type(points) is list:
        points = np.asarray(points)
    if len(points.shape) == 1:
        points = points[:, None]
    med = np.median(points, axis=0)
    abs_dev = np.absolute(points - med)

    med_abs_dev = np.median(abs_dev)

    mod_z_score = norm.ppf(0.75) * abs_dev / med_abs_dev
    return mod_z_score > thresh

def get_mad_outlier(points, thresh=3.5):
    last_index = points.size - 1

    last_ts = points.index[last_index]
    if type(points) is list:
        points = np.asarray(points)
    if len(points.shape) == 1:
        points = points[:, None]
    med = np.median(points, axis=0)
    abs_dev = np.absolute(points - med)

    med_abs_dev = np.median(abs_dev)

    abs_dev_bounds = thresh * med_abs_dev / norm.ppf(0.75)
    abs_upper = med + abs_dev_bounds
    abs_lower = med - abs_dev_bounds

    abs_upper = abs_upper[0] if abs_upper.size == 1 else None
    abs_lower = abs_lower[0] if abs_lower.size == 1 else None

    return abs_upper, abs_lower, points[last_index][0], last_ts