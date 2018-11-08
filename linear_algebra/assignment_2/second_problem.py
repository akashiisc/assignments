import sys

def parse_file(file_name):
    matrix = []
    f = open(file_name).readlines()
    for row in f:
        var = [ int(j) for j in row.strip().split(",")]
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

def find_covarience_matrix(matrix , mean_vector):
    covariece_matrix = []
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


file_name = sys.argv[1]
matrix = parse_file(file_name)
mean_vector = find_mean_vector(matrix)
covarience_vector = find_covarience_matrix(matrix , mean_vector)
print(covarience_vector)

