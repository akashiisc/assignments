
def opr_multiply(X , Y):
    result = []
    for i in range(len(X)):
        result_row = [] 
        for j in range(len(Y[0])):
            result_row.append(0)
        result.append(result_row)

    for i in range(len(X)):
       for j in range(len(Y[0])):
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]

    return result

