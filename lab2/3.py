def delete_minus(x):
    return [[i for i in lists if i > 0] for lists in x]
x = [ [1, -3, -2], [-8, 5], [-1, -4, 3] ]
print(delete_minus(x))

