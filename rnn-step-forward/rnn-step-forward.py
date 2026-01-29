import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    x_t, h_prev, Wx, Wh, b = np.array(x_t), np.array(h_prev), np.array(Wx), np.array(Wh), np.array(b)
    pre = x_t @ Wx + h_prev @ Wh + b
    h_t = np.tanh(pre)
    return h_t.reshape(-1)
