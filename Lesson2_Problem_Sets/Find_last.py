# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search_str, target_str):
    find = -1
    index = 0
    while index <= (len(search_str) - len(target_str)):
        find = search_str.find(target_str, index)
        index += 1

    return find

# print (find_last('aaaa', 'a'))
#>>> 3

# print (find_last('aaaaa', 'aa'))
#>>> 3

# print (find_last('aaaa', 'b'))
#>>> -1

# print (find_last("111111111", "1"))
#>>> 8

# print (find_last("222222222", ""))
#>>> 9

# print (find_last("", "3"))
#>>> -1

print (find_last("", ""))
#>>> 0
