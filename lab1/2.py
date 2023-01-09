upper = 0
lower = 0
text = input()
for i in range(len(text)):
    if text[i].isupper() == True:
        upper += 1
    if text[i].islower() == True:
        lower += 1
print('Upper :' ,upper)
print('Lower :' ,lower)