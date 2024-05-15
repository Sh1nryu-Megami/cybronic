import numpy as np
from scipy.optimize import least_squares


def Triangulation(x1, y1, x2, y2, x3, y3, d1, d2, d3):
    A = np.array([x1, y1])
    B = np.array([x2, y2])
    C = np.array([x3, y3])

    d_A = d1
    d_B = d2
    d_C = d3

    def residuals(p, A, B, C, d_A, d_B, d_C):
        x, y = p
        return [
            np.linalg.norm([x - A[0], y - A[1]]) - d_A,
            np.linalg.norm([x - B[0], y - B[1]]) - d_B,
            np.linalg.norm([x - C[0], y - C[1]]) - d_C,
        ]

    initial_guess = np.mean([A, B, C], axis=0)
    result = least_squares(residuals, initial_guess,
                           args=(A, B, C, d_A, d_B, d_C))
    x, y = result.x
    return (x, y)
