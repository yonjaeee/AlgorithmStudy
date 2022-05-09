import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))
new_graph = graph.copy()

def dfs(graph, new_graph, x, y, num):
    if x >= N or y >= N or x < 0 or y < 0:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        new_graph[y][x] = num
        dfs(graph, new_graph, x-1, y, num)
        dfs(graph, new_graph, x, y-1, num)
        dfs(graph, new_graph, x+1, y, num)
        dfs(graph, new_graph, x, y+1, num)
        return True
    return False
num = 1
for i in range(N):
    for j in range(N):
        if dfs(graph, new_graph, i, j, num) == True:
            num += 1
new_graph_ = new_graph.flatten()
for i in range(1, num):
    print(new_graph_.count(i))
