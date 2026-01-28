import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = comb(n, k) * p**k * (1-p)**(n-k)
    arr1 = np.arange(k + 1)
    cdf = float(np.sum(comb(n, arr1) * (p**arr1) * (1-p)**(n-arr1)))

    return (pmf, cdf)