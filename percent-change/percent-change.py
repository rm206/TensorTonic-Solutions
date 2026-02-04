import numpy as np

def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    series = np.array(series)
    one = series[1:]
    zero = series[:-1]
    res = np.zeros_like(one, dtype=float)
    np.divide(one - zero, zero, out=res, where=zero != 0)
    return res.tolist()