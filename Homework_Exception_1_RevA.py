list_5 = [1, 2, 3, 4, 5]
try:
    print(list_5[7])
except IndexError:
    print('IndexError: list index out of range')