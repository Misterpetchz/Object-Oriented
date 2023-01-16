def count_minus(x):
    count = 0
    for i in range(len(x)):
        count += x[i].count('-')
    return count
print(count_minus(input().split()))