def add2list(lst1,lst2):
    sum = []
    for i in range(len(lst1)):
        sum.append(lst1[i] + lst2[i])
    return sum
print(add2list([int(x) for x in input().split()], [int(x) for x in input().split()]))