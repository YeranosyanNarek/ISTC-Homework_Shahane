for i in range(3):
    try:
        x = int(input())
        y = int(input())
        print(x, '/', y, '=', x / y)
    except ZeroDivisionError:
        print('division by zero')

    except ValueError:
        print("invalid literal for int() with base 10: 'y'")
    except ValueError:
        print("invalid literal for int() with base 10: 'x'")




















