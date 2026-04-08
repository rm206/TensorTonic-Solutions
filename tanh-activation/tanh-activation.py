import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)

    pos = np.exp(x)
    neg = np.exp(-x)

    return (pos - neg)/(pos+neg)