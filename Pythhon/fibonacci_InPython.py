n = int(input())


def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(n):
    print(fibonacci(i))


