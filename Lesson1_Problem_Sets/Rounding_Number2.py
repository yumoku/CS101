# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159
str_x = str(x)

#ENTER CODE BELOW HERE
dot_position = int(str(x).find('.'))
first_decimal = int(str(x).find('.')) + 1

if ("56789".find(str_x[first_decimal]) + 1):
    int_x = int(str_x[0:(dot_position - 1)] + str(int(str_x[dot_position - 1]) + 1))
else:
    int_x = int(str_x[0:dot_position])

print(int_x)

