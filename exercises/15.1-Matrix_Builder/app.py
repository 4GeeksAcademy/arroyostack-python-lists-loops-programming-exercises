#Import random

#Create the function below:

def matrixBuilder(number):
    matrix = []
    for i in range(0, number):
        matrix.append([])
    for i in range(0, number):
        matrix[i].append(([1] * number))

    return sum(matrix, [])


print(matrixBuilder(9))

   