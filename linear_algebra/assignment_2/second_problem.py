import sys
import numpy
#from eigen_values_vector  import *
from myqr import *
from helping_functions import *

def parse_file(file_name):
    matrix = []
    f = open(file_name).readlines()
    for row in f:
        var = [ int(j) for j in row.strip().split(",")]
        var.pop(0)
        matrix.append(var)
    return matrix

def find_mean_vector(matrix):
    mean_vector = []
    width_matrix = len(matrix[0])
    height_matrix = len(matrix)
    i = 0
    while i < width_matrix:
        sum_elements = 0
        j = 0
        while j < height_matrix:
            sum_elements = sum_elements + matrix[j][i]
            j = j + 1
        mean_vector.append(sum_elements/(len(matrix)))
        i = i + 1
    return mean_vector

def find_covarience(matrix , i , j , mean_i , mean_j):
    sum = 0 
    for k in range(len(matrix[0])):
        sum = sum + (matrix[i][k] - mean_i) * (matrix[j][k] - mean_j)
    return sum/(len(matrix[0]))

def find_minus_covarience_matrix(matrix , mean_vector):
    minus_mean_matrix = [];
    width_matrix = len(matrix[0])
    height_matrix = len(matrix)
    for i in range(height_matrix):
        covariece_matrix_row = []
        for j in range(width_matrix):
            #covariece_matrix_row.append(find_covarience(matrix , i , j , mean_vector[i] , mean_vector[j]))
            covariece_matrix_row.append(matrix[i][j] - mean_vector[j]);
        minus_mean_matrix.append(covariece_matrix_row)
    return minus_mean_matrix

def transpose(matrix):
    t = []
    width = len(matrix[0])
    height = len(matrix)
    for i in range(width):
        t_row = []
        for j in range(height):
            t_row.append(matrix[j][i])
        t.append(t_row)
    return t

def multiply(m1 , m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1)):
            row.append(0)
        result.append(row)
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1)):
                result[i][j] = result[i][j] + m1[i][k]*m2[k][j]
    return result

def divide_by_no(matrix , n):
    i = len(matrix)
    j = len(matrix[0])
    r = []
    for a in range(i):
        r_row = []
        for b in range(j):
            r_row.append(matrix[a][b]/n)
        r.append(r_row)
    return r


def remove_first_column(m):
    width = len(m[0])
    height = len(m)
    r = []
    for i in range(height-1):
        r_row = []
        for j in range(width-1):
            r_row.append(m[i+1][j+1])
        r.append(r_row)
    return r


def find_covarience_matrix(matrix , mean_vector):
    covariece_matrix = []
    '''
    width_matrix = len(matrix[0])
    height_matrix = len(matrix)
    i = 0
    while i < width_matrix:
        sum_elements = 0
        j = 0
        while j < height_matrix:
            sum_elements = sum_elements + (matrix[j][i] - mean_vector[i]) * (matrix[j][i] - mean_vector[i])
            j = j + 1
        covariece_matrix.append(sum_elements/(len(matrix)))
        i = i + 1
    return covariece_matrix
    
    width_matrix = len(matrix[0])
    height_matrix = len(matrix)
    for i in range(height_matrix):
        covariece_matrix_row = []
        for j in range(height_matrix):
            covariece_matrix_row.append(find_covarience(matrix , i , j , mean_vector[i] , mean_vector[j]))
        covariece_matrix.append(covariece_matrix_row)
    return covariece_matrix
    '''
    no_of_features = len(matrix) - 1
    minus_mean_matrix = find_minus_covarience_matrix(matrix , mean_vector);
    transpose_minus_mean_matrix = transpose(minus_mean_matrix)
    cov_mat = numpy.dot(transpose_minus_mean_matrix , minus_mean_matrix)
    cov_mat = divide_by_no(cov_mat , no_of_features)
    return cov_mat


file_name = sys.argv[1]
matrix = parse_file(file_name)
matrix = remove_first_column(matrix)
mean_vector = find_mean_vector(matrix)
covarience_vector = find_covarience_matrix(matrix , mean_vector)
#print(covarience_vector)
#print(covarience_vector[97][67])
#print(numpy.cov(numpy.transpose(matrix)))
#print(covarience_vector[0][34])
#matrix = [[2,4,6] , [4, 14,6] , [6,6,28]]
# eigen_values , eigen_vector= eig_by_qr(covarience_vector)
# print(eigen_values)
eigen_values , eigen_vectors = (numpy.linalg.eig(covarience_vector))
unique_eigen_values_with_counts = find_unique_with_counts(eigen_values)
count_of_repeating_eigen_values = get_repeating_values(unique_eigen_values_with_counts)
print(count_of_repeating_eigen_values)

#print(eigen_values)

