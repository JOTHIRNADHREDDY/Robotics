import numpy as np
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
Transpose = np.transpose(matrix)
print("Transpose :",Transpose)

matrix_1 =  np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
Multiplication = np.matmul(matrix, matrix_1)
print("Multiplication : ",Multiplication)