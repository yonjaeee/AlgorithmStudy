# destination에서 sources까지의 거리들 구하는 방식 채택

from collections import deque

def solution(n, roads, sources, destination):
    distances = [-1] * (n+1)
    distances[destination] = 0
    answer = []
    graph = [[] for x in range(n+1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    q = deque([destination])
    while q:
        curr = q.popleft()
        for next_node in graph[curr]:
            if distances[next_node] == -1:
                distances[next_node] = distances[curr] + 1
                q.append(next_node)
    for i in sources:
        answer.append(distances[i])
    return answer