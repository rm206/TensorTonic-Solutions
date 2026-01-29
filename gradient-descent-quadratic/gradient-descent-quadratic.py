def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    curr_x = x0
    new_x = None
    for _ in range(steps):
        new_x = curr_x - (lr * (2 * a * curr_x + b))
        curr_x = new_x
    return new_x