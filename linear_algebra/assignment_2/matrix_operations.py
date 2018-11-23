import numpy 

def opr_multiply(X , Y):
  return numpy.dot(X , Y)
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

def opr_subtract(m1 , m2):
    m = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] - m2[i][j])
        m.append(row)
    return m

def opr_transpose(m):
  rm = []
  for i in range(len(m[0])):
    row = [0] * len(m)
    rm.append(row)
  for i in range(len(m[0])):
    for j in range(len(m)):
      rm[i][j] = m[j][i]
  return rm

