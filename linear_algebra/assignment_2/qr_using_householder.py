import numpy as np

def checkDiagonal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > 0.001:
                    return False
    return True

def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A
 
def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H
 
# task 1: show qr decomp of wp example

a = np.array(((
    (12, -51,   4),
    ( 6, 167, -68),
    (-4,  24, -41),
)))


def eig_by_qr(a):
    a = np.array(a)
    for i in range(100) :
        q, r = qr(a)
        a = np.dot(r,q)
    return q ,r 


#def eig_val_vec(q,r):

x , y = np.linalg.eig(a)
print(x)
print(y)

q , r = eig_by_qr(a)
print(q.round(6))
print(r.round(6))


