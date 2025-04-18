#Write a python program to compute following computation on matrix: a) Addition of two matrices
#b) Subtraction of two matrices c) Multiplication of two matrices d) Transpose of a matrix Code:

import numpy as np
# Initializing matrices
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])
# Matrix addition
print("The element-wise addition of matrices is:")
print(np.add(x, y))
# Matrix subtraction
print("\nThe element-wise subtraction of matrices is:")
print(np.subtract(x, y))
# Matrix multiplication (dot product)
print("\nThe product of matrices is:")
print(np.dot(x, y))
# Transpose of a matrix
print("\nThe transpose of the first matrix is:")
print(x.T)