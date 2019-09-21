import time
import numpy as np

matrix_1 = np.random.rand(3,2)
matrix_2 = np.random.rand(2,3)


matrix = [[0 for x in range(3)] for y in range(3)]  
  


start = time.time()

C = matrix_1.dot(matrix_2)
print(C)

print('\n')


#Test using colummns first
for p in range(len(matrix_1[0])): #0-2  number of columns in matrix_1
	for q in range(len(matrix_1)): #0-3 number of rows in matrix_2
		for r in range(len(matrix_2[0])): #0-3 number of columns in matrix_2
			matrix[q][r] += matrix_1[q][p] * matrix_2[p][r]
for res in matrix:
	print(res)





end = time.time()
print(end - start)

