import numpy as np

# def percentiles(x, q):
#     """
#     Compute percentiles using linear interpolation.
#     """
#     x, q = np.array(x), np.array(q)
#     x = np.sort(x)
#     n = len(x)
#     r = 1 + (n - 1) * (q / 100)
#     k = np.floor(r).astype(int)
#     d = r - k
#     k0 = k - 1
#     k0 = np.clip(k0, 0, n - 2)
#     res = x[k0] + d * (x[k0 + 1] - x[k0])
#     return res

def percentiles(x, q):
    x = np.sort(np.array(x))
    q = np.array(q)
    n = len(x)
    
    idx = (n - 1) * (q / 100.0)
    
    k = np.floor(idx).astype(int)
    d = idx - k
    
    k_up = np.clip(k + 1, 0, n - 1)
    k_low = np.clip(k, 0, n - 1)
    
    return x[k_low] + d * (x[k_up] - x[k_low])

