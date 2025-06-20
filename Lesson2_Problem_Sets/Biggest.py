def bigger(x, y):
    if x > y:
        return x
    return y

def biggest(a, b, c):
    return bigger(bigger(a, b), c)

print(biggest(1, 2, 3))