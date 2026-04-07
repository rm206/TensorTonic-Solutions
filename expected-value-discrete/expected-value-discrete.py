import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if not np.allclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Probabilities must sum to 1.")
    return sum([xi*pi for xi, pi in zip(x, p)])
