import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    x = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(x)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(new_graph, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif new_graph[ny][nx] == 0:
                continue
            else:
                new_graph[ny][nx] = 0
                queue.append((nx, ny))

maxi = 1

# 처음엔 숫자를 줄이려고 2부터 잡았는데
# 예외조건 있음
for i in range(1, 100):
    cnt = 0
    new_graph = []
    for l in range(n):
        new_graph.append([1 if t > i else 0 for t in graph[l]])
    for j in 음ange(n):
        for h in range(n):
            if new_graph[j][h] == 1:
                cnt += 1
                bfs(new_graph, h, j)
    if cnt > maxi:
        maxi = cnt
print(maxi)