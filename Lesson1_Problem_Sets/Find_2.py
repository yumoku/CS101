# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# For example,
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

# text = "all zip files are zipped"
text = 'all zip files are compressed'

#ENTER CODE BELOW HERE
first_occur = text.find("zip")

if first_occur != -1:
    second_occur = text.find("zip", first_occur + 1)
    print(second_occur)












