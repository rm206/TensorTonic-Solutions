import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    v = np.array(values)
    min_val, max_val = np.min(v), np.max(v)

    if min_val == max_val:
        return np.zeros(len(v), dtype=int).tolist()

    bin_width = (max_val - min_val) / num_bins
    indices = np.floor((v - min_val) / bin_width).astype(int)
    res = np.clip(indices, 0, num_bins - 1)
    
    return res.tolist()