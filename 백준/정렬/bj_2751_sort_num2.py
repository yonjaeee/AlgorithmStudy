import sys
import heapq

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
  heapq.heappush(arr, int(sys.stdin.readline()))
for _ in range(N):
  print(heapq.heappop(arr))