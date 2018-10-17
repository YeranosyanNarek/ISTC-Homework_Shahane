list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday ']
for i in range(5):
    try:
        print(list1[i])
    except Exception:
        print('IndexError: list index out of range')