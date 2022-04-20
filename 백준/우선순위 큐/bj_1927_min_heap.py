import sys
import heapq

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, x)
    elif x == 0:
        if len(arr) > 0:
            print(heapq.heappop(arr))
        else:
            print(0)