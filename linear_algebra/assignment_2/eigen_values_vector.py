import numpy

def compute_trace(A) :
    trace = 0 
    for i in range(len(A)):
        trace = trace + A[i][i]
    return trace

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

def subtract(m1 , m2):
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
        for j in range(len(m1)):
            row.append(0)
        result.append(row)
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1)):
                result[i][j] = result[i][j] + m1[i][k]*m2[k][j]
    return result


def find_characteristic_equation_coefficients(matrix) :
    #Faddeev-Leverrier Method
    coefficients = [1]
    B1 = matrix
    for i in range(len(matrix)):
        B = B1
        p = (1/(i+1)) * compute_trace(B)
        coefficients.append(-p)
        m1 = construct_diagonal(p , len(matrix))
        another_one = subtract(B , m1)
        B1 = multiply_matrices(matrix , another_one)
    return coefficients

def solve(coeff_matrix):
    return numpy.roots(coeff_matrix)

def find_eigen_values(matrix):
    characteristic_equation = find_characteristic_equation_coefficients(matrix)
    roots = solve(characteristic_equation)
    return roots


def create_matrix_for_finding_eigen_vector(eigen_value , matrix ) :
    rm = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                rm[i][j] = rm[i][j] 
            else:
                rm[i][j] = rm[i][j] - eigen_value
    return rm

def create_b_matrix(n):
    b = []
    for i in range(n):
        b.append(0)
    return b

def find_eigen_vectors(matrix , eigen_values):
    solutions = []
    for x in eigen_values:
        matrix_for_finding_eigen_vector = create_matrix_for_finding_eigen_vector(x , matrix)
        b_matrix = create_b_matrix(len(matrix));
        solution = numpy.linalg.solve(matrix_for_finding_eigen_vector , b_matrix)
        solutions.append(solution)
    return solutions
