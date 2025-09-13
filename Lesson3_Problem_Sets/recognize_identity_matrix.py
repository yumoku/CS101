# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def is_identity_matrix(input_list):
    # Your code here
    flag = True
    i, j = 0, 0
    i = len(input_list)
    for j in input_list:
        if len(j) != i:
            return False

    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if j == i and input_list[i][j] != 1:
                return False
            elif j != i and input_list[i][j] != 0:
                return False
    return flag

# Test Cases:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
print(is_identity_matrix(matrix1))
# >>>True

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

print(is_identity_matrix(matrix2))
# >>>False

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

print(is_identity_matrix(matrix3))
# >>>False

matrix4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print(is_identity_matrix(matrix4))
# >>>False

matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print(is_identity_matrix(matrix5))
# >>>False

matrix6 = [[1, 0, 0, 0],
           [0, 1, 0, 2],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

print(is_identity_matrix(matrix6))
# >>>False

