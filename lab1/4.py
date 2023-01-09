# x = input("Input your value : ")
# num = x
# sum = 0
# if int(x) < 0 and int(x) > 9:
#     print("Please enter value 0-9")
#     pass
# else:
#     for i in range(4):
#         sum += int(num)
#         num = num + x
# print(sum)

x = int(input("Input your value : "))
if x < 0 and x > 9:
    print("Please enter value 0-9")
    pass
else:
    sum = x + (x + x * 10) + (x + x * 10 + x * 100) + (x + x * 10 + x * 100 + x * 1000)
print(sum)