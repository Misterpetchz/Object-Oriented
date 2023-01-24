def is_plusone_dictionary(d):
    list = []
    for key, value in d.items():
        list.append(key)
        list.append(value)
    for i in range(1, len(list)):
        if list[i] != list[i - 1] + 1:
            return False
    return True
print(is_plusone_dictionary({1:2, 3:4, 5:6, 8:9}))