import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))
out_graph = []
for i in range(n):
    out_graph.append(['R' if g == 'G' else g for g in graph[i]])
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(curr_graph, x, y, color):
    queue = deque()
    queue.append((x, y))
    curr_graph[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif curr_graph[ny][nx] != color:
                continue
            else:
                curr_graph[ny][nx] = 0
                queue.append((nx, ny))

normal_cnt = 0
out_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[j][i] != 0:
            normal_cnt += 1
            bfs(graph, i, j, graph[j][i])

for i in range(n):
    for j in range(n):
        if out_graph[j][i] != 0:
            out_cnt += 1
            bfs(out_graph, i, j, out_graph[j][i])
print(normal_cnt, out_cnt)