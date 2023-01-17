lists = [int(digit) for digit in input().split()]
lists.sort()
for i in range(len(lists)):
    if lists[0] == 0:
        temp = lists[0]
        lists[0] = lists[1]
        lists[i] = temp
print(*lists, sep="")