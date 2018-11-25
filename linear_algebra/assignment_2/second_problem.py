import sys
import numpy
#from eigen_values_vector  import *
from myqr import *
from sklearn.neighbors import KNeighborsClassifier
from helping_functions import *
from matrix_operations import *
from gram_schmidt import *

def parse_file(file_name):
    matrix = []
    label_matrix = []
    f = open(file_name).readlines()
    for row in f:
        var = [ int(j) for j in row.strip().split(",")]
        label_matrix.append(var[0])
        var.pop(0)
        matrix.append(var)
    return matrix , label_matrix

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

def take_first_n_columns(eigen_vectors , n ):
    eigen_vectors_transposed = eigen_vectors.transpose()
    response = []
    for i in range(n):
        response.append(eigen_vectors_transposed[i])
    return np.array(response).transpose()

def sort_eigen_vectors_corresponding_to_sorted_eigen_values(count_of_repeating_eigen_values , eigen_vectors):
    sorted_by_value = sorted(count_of_repeating_eigen_values , reverse=True)
    eigen_vectors_traponsed = np.array(eigen_vectors).transpose()
    sorted_eig_vec_matrix = []
    for x in sorted_by_value:
        for y in count_of_repeating_eigen_values[x]:
            sorted_eig_vec_matrix.append(eigen_vectors_traponsed[y])
    return np.array(sorted_eig_vec_matrix).transpose()

def calculate_reconstruction_error(matrix1 , matrix2):
    sum = 0
    for x in range(len(matrix1)):
        sum_inner = 0
        for y in range(len(matrix1[0])):
            sum_inner = sum_inner + ((matrix1[x][y] - matrix2[x][y])**2)
        sum = sum + sum_inner
    return sum/len(matrix)

def get_labels_corresponding_to_top_m_points(top_m_points , label_matrix):
    labels = []
    for i in top_m_points:
        labels.append(label_matrix[i])
    return labels

output_file_path = "./output_data/output_problem2.txt"
file_to_write = open(output_file_path , 'w')
arguments = sys.argv
if len(arguments) == 3 :
    if arguments[1] == "-type=gram-schimdt":
        gs_matrix = gs_outer(arguments[2])
        print_beautifully(gs_matrix , "" , "" , "" , True , file_to_write , "list_of_list")
        exit()
    else :
        print("Unknown Input")
        exit(1)

file_name = sys.argv[1]
output_plot_dir = "./output_plots/"
matrix , label_matrix = parse_file(file_name)
#matrix = remove_first_column(matrix)
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
sorted_eigen_vectors = sort_eigen_vectors_corresponding_to_sorted_eigen_values(unique_eigen_values_with_counts , eigen_vectors)

reconstruction_error_map = {}
for i in range(1, 10 , 1) :
    top_m_eigen_vectors = take_first_n_columns(sorted_eigen_vectors , i)
    reduced_dimention_matrix = opr_multiply(matrix , top_m_eigen_vectors)
    if i == 2:
        plot_scatter_graph(reduced_dimention_matrix , label_matrix , True , output_plot_dir+"problem_2_bonus_1.png" )
    appended_matrix = append_m_columns(reduced_dimention_matrix , len(matrix[0])-i)
    reconstruction_error = calculate_reconstruction_error( matrix, appended_matrix)
    reconstruction_error_map[i] = reconstruction_error

for i in range(10, 500 , 10) :
    top_m_eigen_vectors = take_first_n_columns(sorted_eigen_vectors , i)
    reduced_dimention_matrix = opr_multiply(matrix , top_m_eigen_vectors)
    appended_matrix = append_m_columns(reduced_dimention_matrix , len(matrix[0])-i)
    reconstruction_error = calculate_reconstruction_error( matrix, appended_matrix)
    reconstruction_error_map[i] = reconstruction_error

task_plot_graph(reconstruction_error_map , True ,  output_plot_dir+"problem_2_task_5.png" , "Dimension" , "Reconstruction error"  , "Reconstrunction error")
print_barrier(file_to_write)
print_beautifully(reconstruction_error_map , "Reconstruction Error" , "Dimentionality Reduction" , "Reconstruction error" , True , file_to_write , "map")
print_barrier(file_to_write)

converted_mean_vector_to_matrix = []
for i in range(len(matrix)):
    a = copy(mean_vector)
    converted_mean_vector_to_matrix.append(a)

print(len(mean_vector))
print(len(converted_mean_vector_to_matrix))
print(len(converted_mean_vector_to_matrix[0]))
converted_minus_mean_matrix = opr_subtract(matrix , converted_mean_vector_to_matrix)
print(len(converted_minus_mean_matrix))

'''

############################################################################################
#                                                                                          #          
#                  K-NN Code Yipieeeeeeeeeeeee                                             #
#                                                                                          #
############################################################################################
# First doing it for complete data without reduction                                       #
# Taking first 9000 for training and last 1000 for teting                                  #
############################################################################################

print_barrier(file_to_write)

# m_values = range(20,30)
# k_values = [1,3,5,10,15,20]
m_values = range(30,35)
k_values = [1,3]
for m in m_values:
    top_m_eigen_vectors = take_first_n_columns(sorted_eigen_vectors , m)
    reduced_dimention_matrix = opr_multiply(matrix , top_m_eigen_vectors)
    reduced_dimention_matrix = np.array(reduced_dimention_matrix).real
    mean_vector_of_reduced = find_mean_vector(reduced_dimention_matrix)

    converted_mean_vector_to_matrix = []
    for j in range(len(matrix)):
        a = copy(mean_vector_of_reduced)
        converted_mean_vector_to_matrix.append(a)
    converted_minus_mean_matrix = opr_subtract(reduced_dimention_matrix, converted_mean_vector_to_matrix)
    correctness_difference_vector = {}
    for k in k_values:
        correctness_difference_vector[k] = []
    for i in range(8000 , 10000):
        squared_distance_from_all = {}
        for j in range(8000):
            squared_distance = calculate_square_distance(converted_minus_mean_matrix , i , j)
            squared_distance_from_all[j] = squared_distance
        sorted_squared_distance_from_all = sorted(squared_distance_from_all.items(), key=lambda x: x[1])
        for k in k_values:
            top_m_points = take_top_m_points(sorted_squared_distance_from_all , k)
            labels_corresponding_to_top_m_points = get_labels_corresponding_to_top_m_points(top_m_points , label_matrix)
            majority_element = find_majority(labels_corresponding_to_top_m_points)
            correctness_difference_vector[k].append(majority_element - label_matrix[i])
    for k in k_values:
        non_zero_elements = numpy.count_nonzero(correctness_difference_vector[k])
        accuracy = (len(correctness_difference_vector[k])-non_zero_elements) / len(correctness_difference_vector[k])
        print( str(m) + "," + str(k) + "," + str(accuracy))

print_barrier(file_to_write)
'''
############################################################################################
#                                                                                          #          
#                  K-NN Code Sklearn                                                      #
#                                                                                          #
############################################################################################
# First doing it for complete data without reduction                                       #
# Taking first 9000 for training and last 1000 for teting                                  #
############################################################################################

print_barrier(file_to_write)

m_values = range(1,50)
k_values = [1,3,5,10,15,20]

for m in m_values:
    top_m_eigen_vectors = take_first_n_columns(sorted_eigen_vectors , m)
    reduced_dimention_matrix = opr_multiply(matrix , top_m_eigen_vectors)
    reduced_dimention_matrix = np.array(reduced_dimention_matrix).real
    mean_vector_of_reduced = find_mean_vector(reduced_dimention_matrix)
    converted_mean_vector_to_matrix = []
    for j in range(len(matrix)):
        a = copy(mean_vector_of_reduced)
        converted_mean_vector_to_matrix.append(a)
    converted_minus_mean_matrix = opr_subtract(reduced_dimention_matrix , converted_mean_vector_to_matrix)
    for k in k_values:
        correctness_difference_vector = []
        neigh = KNeighborsClassifier(n_neighbors=k)
        neigh.fit(converted_minus_mean_matrix[:8000], label_matrix[:8000])
        for i in range(8001 , 10000):
            majority_element = neigh.predict([converted_minus_mean_matrix[i]])
            correctness_difference_vector.append(majority_element[0] - label_matrix[i])
        non_zero_elements = numpy.count_nonzero(correctness_difference_vector)
        accuracy = (len(correctness_difference_vector)-non_zero_elements) / len(correctness_difference_vector)
        print( str(m) + "," + str(k) + "," + str(accuracy))

print_barrier(file_to_write)
# For each m starting from 1 to m 
#top_m_eigen_values = get_top_m_values(unique_eigen_values_with_counts , 4)
#print(top_m_eigen_values)
#vector_corresponding_to_top_m_eigen_values = build_vector_corresponding_to_values(top_m_eigen_values , count_of_repeating_eigen_values , eigen_vectors)