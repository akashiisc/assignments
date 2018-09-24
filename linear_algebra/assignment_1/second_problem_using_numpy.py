import sys
import numpy
import time

file_name_for_input = sys.argv[1]
f = open(file_name_for_input)
of = open("output_problem2_numpy.txt" , "w")

size_of_matrix = int(f.readline().strip())
i=0
matrix = []
while i < size_of_matrix :
    matrix_row = [float(x) for x in f.readline().strip().split()]
    matrix.append(matrix_row)
    i = i+1

start_time = time.clock()
inverse = numpy.linalg.inv(matrix)
end_time = time.clock()

print end_time - start_time
i=0
while i < size_of_matrix:
    j = 0
    while j < size_of_matrix :
        #sys.stdout.write(str(inverse[i][j]))
        of.write(str(inverse[i][j]))
        #sys.stdout.write(" ")
        of.write(" ")
        j = j+1
    #print ""
    of.write("\n")
    i = i+1

