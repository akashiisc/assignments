import sys
import random

def swap(M , row , column):
    temp = M[row]
    M[row] = M[column]
    M[column] = temp
    return M

def multiply(M , row , value):
    i = 0
    while i < len(M[row]):
        M[row][i] = value * M[row][i]
        i = i+1
    return M

def add(M , row1 , row2 , factor):
    i = 0
    while i < len(M[row1]):
        M[row1][i] = M[row1][i] + factor * M[row2][i]
        i=i+1
    return M

def first_non_zero_row(M , start_row , start_column , end_row ):
    ginti = start_row
    found_in_row = -1
    while ginti <= end_row:
        if M[ginti][start_column]!=0:
            found_in_row = ginti
            break
        else:
            ginti = ginti + 1
    return found_in_row


def convert_to_echelon_form_utility(M , start_row , start_column , end_row , end_column , row_operations):
    # type: (object, object, object, object, object) -> object
    # exit form the function when start_row > end_row || start_column > end_column
    #
    # search for the nonzero element in the column
    # if the non zero element is not found in the start row swap the row with the first row
    # if no non zero element found in the column move to next column with the same row
    #     call convert_to_echelon_form(M , start_row , start_column+1 , end_row , end_column)
    # try to make all the elements below this in the column as 0
    # move to next iteration with convert_to_echelon_form(M , start_row+1 , start_column+1 , end_row , end_column)
    # print "\n=====iteration====="
    # print start_row
    # print start_column
    # print end_row
    # print end_column
    # print M

    if start_row > end_row or start_column > end_column:
        return (M , row_operations)

    first_non_zero_row_entry = first_non_zero_row(M , start_row , start_column , end_row)
    if first_non_zero_row_entry == -1:
        return convert_to_echelon_form_utility(M, start_row, start_column + 1, end_row, end_column , row_operations)
    elif first_non_zero_row_entry != start_row:
        row_operations.append("SWITCH " + str(start_row) + " " + str(first_non_zero_row_entry))
        M = swap(M , start_row , first_non_zero_row_entry)

    row_operations.append("MULTIPLY " + str(start_row) + str(1 / M[first_non_zero_row_entry][start_column]) + " " + str(start_row))
    M = multiply(M , start_row , 1/M[first_non_zero_row_entry][start_column])
    current_row = start_row+1
    while current_row <= end_row:
        if M[current_row][start_column] != 0:
            row_operations.append(
                "MULTIPLY AND ADD " + str(-M[current_row][start_column]) + " " + str(
                    start_row) + " " + str(current_row))
            M = add(M , current_row , start_row , -M[current_row][start_column])
        current_row = current_row + 1
    return convert_to_echelon_form_utility(M, start_row+1, start_column+1, end_row, end_column, row_operations)

def convert_to_echelon_form(M , start_row , start_column , end_row , end_column):
    row_operations = []
    return convert_to_echelon_form_utility(M , start_row , start_column , end_row , end_column , row_operations)

def try_to_make_max_zeros_except_the_ones_utility(matrix , start_row , start_column , end_row , end_column , pivot_entries , row_operations):
    for (x,y) in pivot_entries:
        # make all entries above the pivot to be zero
        counter = x - 1
        while counter >= 0:
            if matrix[counter][y] != 0 :
                row_operations.append("MULTIPLY AND ADD " + str(- matrix[counter][y] / matrix[x][y]) + " " + str(
                    x) + " " + str(counter))
                matrix = add(matrix , counter , x , -matrix[counter][y] / matrix[x][y])
            counter = counter - 1
    return (matrix , row_operations)

def try_to_make_max_zeros_except_the_ones(matrix , start_row , start_column , end_row , end_column , pivot_entries):
    row_operations = []
    return try_to_make_max_zeros_except_the_ones_utility(matrix , start_row , start_column , end_row , end_column , pivot_entries , row_operations)

def find_pivot_element_in_row(M , row , start_column , end_column):
    i = start_column
    found_element = -1
    while i<=end_column :
        if M[row][i] != 0:
            found_element = i
            break
        i = i + 1
    return found_element

def find_pivot_columns_utility(M , start_row , start_column , end_row , end_column , pivot_columns):
    # if start_row > end_row:
    # exit with returning pivot_columns
    # find pivot in first row
    # if pivot_found :
    #    insert pair(column,row) into the pivot_columns_list
    #    call find_pivot_columns_utility(M , start_row+1 , pivot_column+1 , end_row , end_column , pivot_columns)
    # else :
    #    return pivot_columns and exit
    if start_row > end_row:
        return pivot_columns

    pivot_element_in_row = find_pivot_element_in_row(M , start_row , start_column , end_column) # essentially the column
    if pivot_element_in_row == -1:
        return pivot_columns

    pair_row_col = (start_row,pivot_element_in_row)
    pivot_columns.append(pair_row_col)
    return  find_pivot_columns_utility(M , start_row+1 , pivot_element_in_row+1 , end_row , end_column , pivot_columns)

def find_pivot_columns(solition , start_row , start_column , end_row , end_column):
    pivot_columns = []
    return find_pivot_columns_utility(solition , start_row , start_column , end_row , end_column , pivot_columns)

file_name_for_input = sys.argv[1]
f = open(file_name_for_input)

size_of_matrix = int(f.readline().strip())
i=0
matrix = []
while i < size_of_matrix :
    matrix_row = [float(x) for x in f.readline().strip().split()]
    j = 0
    while j < size_of_matrix :
        if i == j:
            matrix_row.append(1)
        else:
            matrix_row.append(0)
        j = j+1
    matrix.append(matrix_row)
    i = i+1

(matrix , row_operations) = convert_to_echelon_form(matrix , 0 , 0 , size_of_matrix-1 , size_of_matrix-1)
pivots = find_pivot_columns(matrix , 0 , 0 , size_of_matrix-1 , size_of_matrix-1)
(matrix , row_operations_1) = try_to_make_max_zeros_except_the_ones(matrix , 0 , 0 , size_of_matrix-1 , size_of_matrix-1 , pivots)
pivots = find_pivot_columns(matrix , 0 , 0 , size_of_matrix-1 , size_of_matrix-1)
if len(pivots) == size_of_matrix :
    print "YAAY! FOUND ONE !"
    i = 0
    while i < size_of_matrix:
        j = size_of_matrix
        while j < 2*size_of_matrix :
            sys.stdout.write(str(matrix[i][j]))
            sys.stdout.write(" ")
            j = j+1
        print ""
        i = i+1
elif len(pivots) < size_of_matrix:
    print "ALAS! DIDN'T FIND ONE!"
    for x in row_operations:
        print x
    for x in row_operations_1:
        print x


