import numpy as np
from collections import Counter

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if not y:
        return 0.0

    _, counts = np.unique(y, return_counts = True)

    probs = counts / len(y)
    return -np.sum(probs * np.log2(probs))