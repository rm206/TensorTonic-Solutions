import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x, gamma, beta = np.array(x), np.array(gamma), np.array(beta)

    if x.ndim == 2:
        axis = 0
    else:
        axis = (0, 2, 3)

    mean = np.mean(x, axis = axis, keepdims=True)
    var = np.var(x, axis = axis, keepdims=True)

    xhat = (x-mean) / np.sqrt(var + eps)

    gr = gamma.reshape(mean.shape)
    br = beta.reshape(mean.shape)

    return gr * xhat + br