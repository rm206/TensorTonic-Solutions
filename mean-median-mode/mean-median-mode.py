import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x)
    vals, cnts = np.unique_counts(x)
    return (np.mean(x), np.median(x), float(vals[np.argmax(cnts)]))