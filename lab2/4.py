def count_minus(x):
    return sum([i.count('-') for i in x.split()])
    #return len([i for i in num if i < 0]) must int input 
print(count_minus(input()))