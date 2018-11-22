import numpy as np

def qr_householder(A):
    m, n = A.shape
    Q = np.eye(m) # Orthogonal transform so far
    R = A.copy() # Transformed matrix so far

    for j in range(n):
        # Find H = I - beta*u*u' to put zeros below R[j,j]
        x = R[j:, j]
        normx = np.linalg.norm(x)
        rho = -np.sign(x[0])
        u1 = x[0] - rho * normx
        u = x / u1
        u[0] = 1
        beta = -rho * u1 / normx

        R[j:, :] = R[j:, :] - beta * np.outer(u, u).dot(R[j:, :])
        Q[:, j:] = Q[:, j:] - beta * Q[:, j:].dot(np.outer(u, u))
        
    return Q, R

def eig_by_qr(a):
    a = np.array(a)
    i = 100
    while(i>0):
        q, r = qr_householder(a)
        a = np.dot(r,q)
        i = i -1
    return q ,r


a = np.array(((
    (12, -51,   4),
    ( 6, 167, -68),
    (-4,  24, -41),
)))

x , y = np.linalg.eig(a)
print(x)
print(y)

q , r = eig_by_qr(a)
print(q)
print(r)

