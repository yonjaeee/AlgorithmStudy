import sys
import heapq

t = int(sys.stdin.readline())
for test in range(t):
    n = int(sys.stdin.readline())
    rank = []
    for p in range(n):
        rk = tuple(map(int, sys.stdin.readline().strip().split()))
        heapq.heappush(rank, rk)
    result = 0
    mini = 0
    for p in range(n):
        a, b = heapq.heappop(rank)
        if mini == 0:
            mini = b
            result += 1
        elif b < mini:
            mini = b
            result += 1
    print(result)