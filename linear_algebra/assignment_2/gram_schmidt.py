import sys
import numpy
from eigen_values_vector import *

def parse_file_gs(file_name):
    matrix = []
    f = open(file_name).readlines()
    for row in f:
        var = [ float(j) for j in row.strip().split(" ")]
        matrix.append(var)
    return matrix


def gs_cofficient(v1, v2):
    return numpy.dot(v2, v1) / numpy.dot(v1, v1)

def multiply(cofficient, v):
    return map((lambda x : x * cofficient), v)

def proj(v1, v2):
    return multiply(gs_cofficient(v1, v2) , v1)

def gs(X):
    Y = []
    for i in range(len(X)):
        temp_vec = X[i]
        for inY in Y :
            proj_vec = list(proj(inY, X[i]))
            temp_vec = list(map(lambda x, y : x - y, temp_vec, proj_vec))
        Y.append(temp_vec)
    return Y

def gs_outer(file_name):
    matrix = parse_file_gs(file_name)
    x = gs(matrix)
    return x
