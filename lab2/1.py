lists = [int(digit) for digit in input().split()]
lists.sort()
for i in range(len(lists)):
    if lists[0] == 0:
        lists[i],lists[0] = lists[0],lists[i]
print(*lists, sep="")