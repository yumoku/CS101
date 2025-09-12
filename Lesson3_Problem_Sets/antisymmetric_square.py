# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(input_list):
    # Your code here
    flag = True
    i, j = 0, 0
    i = len(input_list)
    for j in input_list:
        if len(j) != i:
            return False

    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i][j] != -input_list[j][i]:
                return False
    return flag

# Test Cases:

print (antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
#>>> True

print (antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print (antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
#>>> False

print (antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False
