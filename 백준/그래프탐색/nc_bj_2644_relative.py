import sys

n = int(sys.stdin.readline())
f, s = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    parent, son = map(int, sys.stdin.readline().strip().split())
    graph[parent].append(son)

# DFS
