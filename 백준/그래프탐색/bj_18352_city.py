# bfs로  풀자
import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    graph[start].append(end)

d = [0] * (N+1)
cur = 0
q = deque([X])
while cur < K:
    q.popleft()
    for 

    cur += 1
