import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    w, g, G = np.array(w), np.array(g), np.array(G)
    
    G_new = G + g**2
    w_new = w - ((lr/(G_new + eps)**0.5) * g)

    return (w_new, G_new)