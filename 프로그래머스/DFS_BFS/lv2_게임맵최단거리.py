# BFS
from collections import deque

def solution(maps):
    graph = maps
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        curr_x, curr_y = q.popleft()
        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if graph[next_y][next_x] == 0:
                continue
            if graph[next_y][next_x] == 1:
                graph[next_y][next_x] = graph[curr_y][curr_x] + 1
                q.append((next_x, next_y))
    if graph[n-1][m-1] < n+m-1:
        return -1
    else:
        return graph[n-1][m-1]