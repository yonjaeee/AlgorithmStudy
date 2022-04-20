import heapq
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, -x)
    elif x == 0:
        if len(arr) > 0:
            print(-1 * heapq.heappop(arr))
        else:
            print(0)