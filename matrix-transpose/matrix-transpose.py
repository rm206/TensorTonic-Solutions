import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n, m = len(A[0]), len(A)
    res = np.zeros((n, m))

    for i in range(len(A)):
        for j in range(len(A[0])):
            res[j][i] = A[i][j]

    return res