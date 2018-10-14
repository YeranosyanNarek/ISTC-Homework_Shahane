username = input('username')

class MyException(Exception):
    pass
try:
    if username == 'Rembo':
        raise MyException

    else:
        print('welcome ', username)

except MyException:
    print('Rambo is an invalid username')


