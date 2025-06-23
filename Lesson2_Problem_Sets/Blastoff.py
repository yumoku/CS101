# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(i):
    while i > 1:
        i -= 1
        print(i)
    print('Blastoff!')



countdown(13)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!