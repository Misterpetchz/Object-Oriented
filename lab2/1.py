lists = []
lists = [int(digit) for digit in input().split()]
for x in range(len(lists)):
    for y in range(len(lists)):
        if lists[x] < lists[y]:
            temp = lists[y]
            lists[y] = lists[x]
            lists[x] = temp

for i in range(len(lists)):
    if lists[0] == 0:
        temp = lists[0]
        lists[0] = lists[1]
        lists[i] = temp
print(*lists, sep="")