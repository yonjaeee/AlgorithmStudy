import sys

d = [(0, 0) for x in range(41)]

def fibonacci(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    if d[n] != (0, 0):
        return d[n]
    else:
        d[n] = tuple(sum(e) for e in zip(fibonacci(n-1), fibonacci(n-2)))
        return d[n]

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    zero, one = fibonacci(n)
    print(zero, one)
