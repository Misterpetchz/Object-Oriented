num = []
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        value = str(x*y)
        if value == value[::-1]:
            num.append(x*y)
print(max(num))