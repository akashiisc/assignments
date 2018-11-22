import numpy as np
import math

def checkDiagonal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > 0.0000000001:
                    return False
    return True

def construct_diagonal(p , size):
    dia = []
    for i in range(size):
        row = []
        for j in range(size):
            if i  == j:
                row.append(p)
            else :
                row.append(0)
        dia.append(row)
    return dia

def subtract_matrices(m1 , m2):
    m = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1)):
            row.append(m1[i][j] - m2[i][j])
        m.append(row)
    return m

def multiply_matrices(m1 , m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            row.append(0)
        result.append(row)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] = result[i][j] + m1[i][k]*m2[k][j]
    return result

def multiply_scalar(scalar , m):
    result = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(0)
        result.append(row)
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[i][j] = scalar * m[i][j]
    return result

def construct_identity(size):
    return construct_diagonal(1,size)

def calculate_d(matrix , i):
    d = 0
    j = i
    while(j<len(matrix)):
        d = d + matrix[j] * matrix[j]
        j = j + 1
    return math.sqrt(d)

def qr_algo(A):
    A_transpose = A.transpose();
    rows = len(A)
    cols = len(A[0])
    pi_a_matrix = A
    for i in range(cols-1):
        pi_a_matrix_tranapose = pi_a_matrix.transpose()
        col_i = pi_a_matrix_tranapose[i]
        col_i = col_i / np.linalg.norm(col_i)
        diagonal_element = col_i[i]
        D = calculate_d(col_i , i)
        if diagonal_element > 0 :
            D = -D
        v_matrix = []
        for j in range(i):
            v_matrix.append(0)
        v_k = math.sqrt(0.5 * (1- (col_i[i]/D)))
        v_matrix.append(v_k)
        p = -D * v_k
        for k in range(cols-i-1):
            v_k_j = col_i[i+k+1]/(2*p)
            v_matrix.append(v_k_j)
        v_matrix = np.asarray(v_matrix)
        v_matrix_transpose = v_matrix.transpose().reshape((cols,1))
        v_matrix = v_matrix.reshape((1,cols))
        multiplied_res =  multiply_matrices(v_matrix_transpose , v_matrix)
        scalar_multiplied_matrix = multiply_scalar(2 , multiplied_res)
        identity_matrix = np.asarray(construct_identity(rows))
        p_matrix = subtract_matrices(identity_matrix , scalar_multiplied_matrix)
        if i == 0:
            p_matrix_multiplied = p_matrix
        else :
            p_matrix_multiplied = multiply_matrices(p_matrix , p_matrix_multiplied)
        pi_a_matrix = np.asarray(multiply_matrices(p_matrix , pi_a_matrix))
    return np.asarray(p_matrix_multiplied).transpose() , np.asarray(pi_a_matrix)


def get_eig_values(m):
    vals = []
    for i in range(len(m)):
        vals.append(m[i][i])
    return vals

def eig_by_qr(a):
    a = np.array(a)
    i = 0
    while(True):
        q, r = qr_algo(a)
        if i == 0:
            multiplication_of_qs = np.array(q).transpose()
        else :
            multiplication_of_qs = multiply_matrices( np.array(q).transpose() , multiplication_of_qs)
        a = np.array(multiply_matrices(r,q))
        i = i + 1
        if(checkDiagonal(a)) : 
            break;
    #print("Converged after " + str(i) + "times")
    eig_vals = get_eig_values(a)
    #eig_vectors = get_eig_vectors(multiplication_of_qs)
    return eig_vals , multiplication_of_qs


'''
A = np.array([[2,1,1],[1,2,1],[1,1,2]]);
a , b = qr_algo(A)
print(a.round(4))
print(b.round(4))

m , n = np.linalg.eig(A)
print(m)
print(n)

eig_vals , eig_vectors = eig_by_qr(A)
print(np.array(eig_vals).round(4))
print(np.array(eig_vectors).round(4))
'''
