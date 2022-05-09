# Recursion Error 떴었는데 이는 최대 깊이보다 더 탐색해야 되서
# sys.setrecursionlimit()으로 해결
import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

def dfs(graph, x, y):
    if x >= m or y >= n or x < 0 or y < 0:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(graph, x - 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x + 1, y)
        dfs(graph, x, y + 1)
        return True
    return False

for _ in range(T):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().strip().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = 1
    for i in range(m): 
        for j in range(n):
            if dfs(graph, i, j) == True:
                cnt += 1
    print(cnt)