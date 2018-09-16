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


def convert_to_echelon_form(M , start_row , start_column , end_row , end_column):
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
        return M

    first_non_zero_row_entry = first_non_zero_row(M , start_row , start_column , end_row)
    if first_non_zero_row_entry == -1:
        return convert_to_echelon_form(M, start_row, start_column + 1, end_row, end_column)
    elif first_non_zero_row_entry != start_row:
        M = swap(M , start_row , first_non_zero_row_entry)
        first_non_zero_row_entry = start_row
    M = multiply(M , start_row , 1/M[first_non_zero_row_entry][start_column])
    current_row = start_row+1
    while current_row <= end_row:
        if M[current_row][start_column] != 0:
            M = add(M , current_row , start_row , -M[current_row][start_column])
        current_row = current_row + 1
    return convert_to_echelon_form(M, start_row+1, start_column+1, end_row, end_column)

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

def solve_for_unique_solution(solution , pivot_columns , end_column):
    variable_assignments = {}
    for (x,y) in reversed(pivot_columns):
        subtract_value = 0
        from_column = y+1
        while from_column <= end_column-1:
            subtract_value = subtract_value + solution[x][from_column] * variable_assignments[from_column]
            from_column = from_column+1
        variable_assignments[y] = round(solution[x][end_column] - subtract_value , 3)
    return variable_assignments

def solve_for_many_solutions(solution , pivot_columns , end_column ):
    trials = 0
    max_trials = 100
    basic_variables = []
    free_variables = []
    pivot_columns = filter(lambda x: check_within(x, len(solution[0]) - 1), pivot_columns)
    for (x, y) in pivot_columns:
        if (y < end_column):
            basic_variables.append(y)
    for x in range(len(solution[0]) - 1):
        if x not in basic_variables:
            free_variables.append(x)
    generalized_solution = []
    for x in free_variables:
        generalized_solution.append("i"+str(x))
    for (x, y) in reversed(pivot_columns):
        subtract_string = ""
        from_column = y + 1
        while from_column <= end_column - 1:
            if(subtract_string == ""):
                subtract_string = subtract_string + str(solution[x][from_column]) + "i" + str(from_column)
            else :
                subtract_string = subtract_string + " + (" + str(solution[x][from_column]) + "i" + str(from_column) + ")"
            from_column = from_column + 1
        generalized_solution.append("i"+str(y)+" = "+ str(solution[x][end_column]) + "-" + "( " + subtract_string + " )" )

    while trials < max_trials:
        variable_assignments = {}
        for x in free_variables:
            variable_assignments[x] = random.randint(1,max_quantities[x])
        for (x,y) in reversed(pivot_columns):
            subtract_value = 0
            from_column = y+1
            while from_column <= end_column-1:
                subtract_value = subtract_value + solution[x][from_column] * variable_assignments[from_column]
                from_column = from_column+1
            variable_assignments[y] = round(solution[x][end_column] - subtract_value , 3)
        (possibility,rejection_type) = check_for_the_inequalities(variable_assignments, max_quantities)
        if possibility == True:
            return (possibility , variable_assignments , generalized_solution)
        trials = trials + 1
    return (False , {} , generalized_solution)


def check_for_the_inequalities(variable_assignments , max_quantities):
    possiblity = True
    rejection_type = 0
    for key in variable_assignments:
        if variable_assignments[key] > max_quantities[key] :
            possiblity = False
            rejection_type = 1
        elif variable_assignments[key] < 0 :
            possiblity = False
            rejection_type = 2
    return (possiblity , rejection_type)

def check_within(list_element , max_value):
    return list_element[1] < max_value


part = sys.argv[1]
file_name_for_input = sys.argv[2]
f = open(file_name_for_input)

if part == "--part=one":
    n=4
    k=4
elif part == "--part=two":
    t = f.readline()
    t = t.strip()
    nk_value = [x for x in t.split()]
    n = int(nk_value[0])
    k = int(nk_value[1])

quantities = [float(x) for x in f.readline().strip().split()]
percentages = []

i=0
while i < n :
    #percentages_row = [float(x) for x in raw_input().split()]
    percentages_row = [float(x) for x in f.readline().strip().split()]
    percentages_row.append(quantities[i])
    percentages.append(percentages_row)
    i = i+1

#max_quantities = [float(x) for x in raw_input().split()]
max_quantities = [float(x) for x in f.readline().strip().split()]

solution = convert_to_echelon_form(percentages ,  0 , 0 , len(percentages)-1 , len(percentages[0])-1)
pivot_columns = find_pivot_columns(solution , 0 , 0 , len(solution)-1 , len(solution[0])-1)
if len(pivot_columns) == len(solution[0]):
    print "NOT POSSIBLE,SNAPE IS WICKED!"
elif len(pivot_columns) == len(solution[0])-1:
    pivot_columns = filter(lambda x:check_within(x , len(solution[0])-1) , pivot_columns)
    variable_assignments = solve_for_unique_solution(solution , pivot_columns , len(solution[0])-1)
    (possibility , rejection_type) = check_for_the_inequalities(variable_assignments , max_quantities)
    if possibility == True:
        print "EXACTLY ONE!"
        for x in variable_assignments:
            sys.stdout.write(str(variable_assignments[x]))
            sys.stdout.write(" ")
    else :
        print "NOT POSSIBLE,SNAPE IS WICKED!"
else: # case when there are some free variables
    (possibility , variable_assignments , generalized_solution) = solve_for_many_solutions(solution , pivot_columns , len(solution[0])-1)
    if possibility == True:
        print "MORE THAN ONE!"
        for x in variable_assignments:
            sys.stdout.write(str(variable_assignments[x]))
            sys.stdout.write(" ")
        print ""
        generalized_solution_string = ",".join(generalized_solution)
        print generalized_solution_string
