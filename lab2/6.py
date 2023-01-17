def add2list(lst1,lst2):
    return [lst1[i] + lst2[i] for i in range(len(lst1))]
print(add2list([int(x) for x in input().split()], [int(x) for x in input().split()]))