import numpy as np

def qr_factorization(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]

        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q.dot(v)
            v = v - R[i, j] * q

        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R

A = np.random.rand(13, 10) * 1000
Q, R = qr_factorization(A)

print(Q)
print(R)
Q.shape, R.shape
np.abs((A - Q.dot(R)).sum()) < 1e-6
