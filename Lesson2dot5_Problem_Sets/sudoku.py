# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

def check_uniqueness(input_list):
    """
    This method is to check if
    there are duplicate elements
    in a list
    """
    flag = True
    if len(input_list) != len(set(input_list)):
        flag = False
    return flag

def check_sudoku(input_numbers):
    """
    check if input numbers match sudoku
    """
    flag = True
    length = len(input_numbers)
    column = []
    #check if input elements are in the correct range
    for i in input_numbers:
        for j in i:
            if j not in list(range(1, (length + 1))):
                flag = False
                return False

    #check if input is square or not
    for row in input_numbers:
        if len(row) != length:
            flag = False
            return False

    # check if each row is unique
    for row in input_numbers:
        flag *= check_uniqueness(row)
        if flag is False:
            return False

    # check if each column is unique
    for i in range(0, length):
        for j in range(0, length):
            column.append(input_numbers[j][i])
        flag *= check_uniqueness(column)
        if flag is False:
            return False

        column =[]

    return True










print (check_sudoku(incorrect))
# >>> False

print (check_sudoku(correct))
# >>> True

print (check_sudoku(incorrect2))
# >>> False

print (check_sudoku(incorrect3))
# >>> False

print (check_sudoku(incorrect4))
# >>> False

print (check_sudoku(incorrect5))
# >>> False
