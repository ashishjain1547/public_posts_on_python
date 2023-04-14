def division(a, b):
    print("a:", a)
    print("b:", b)
    if b == 0:
        raise Exception
    return a/b

try:
    print("Success:", division(5, 5))
    division(5, 0)
except ZeroDivisionError as err:
     print('Handling run-time error:', err)

