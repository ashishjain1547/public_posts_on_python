n = input("Enter n: ")

def fib(n):
    cur = 1
    old = 1
    i = 1
    while (i < n):
        cur, old, i = cur+old, cur, i+1
    return cur

print("Fibonacci numbers:")
fib_list = list()
for i in range(int(n)):
    fib_list.append(str(fib(i)))

print(' '.join(fib_list))