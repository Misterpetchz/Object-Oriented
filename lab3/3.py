def is_plusone_dictionary(d):
    for i in range(len(d)):
        if [x for x in d.keys()][i] != [x for x in d.values()][i] - 1:
            return False
    return True
print(is_plusone_dictionary({1:2, 3:4, 5:6, 7:8}))