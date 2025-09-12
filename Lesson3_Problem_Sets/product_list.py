# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(input: list[int]):
    result = 1
    for element in input:
        result *= element

    return result

# print (product_list([9]))
#>>> 9

# print (product_list([1,2,3,4]))
#>>> 24

print (product_list([]))
#>>> 1

