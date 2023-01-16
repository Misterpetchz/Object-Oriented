def count_char_in_string(x,c):
    count = []
    for i in range(len(x)):
        str = x[i].count(c)
        count.append(str)
    return count
print(count_char_in_string(input().split(),input()))