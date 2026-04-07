import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    w, g, s = np.array(w), np.array(g), np.array(s)

    s_new = beta * s + (1 - beta) * g**2
    w_new =  w - ((lr/(s_new + eps)**0.5) * g)

    return (w_new, s_new)