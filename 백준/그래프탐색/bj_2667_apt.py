import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))
  
def dfs(x, y):
    # global 변수 선언을 통하여 local 변수 때문에 또다른 리스트나 배열 만들어야 하는 수고로움 덜음
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        count += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

count = 0
count_list = []

for x in range(n):
    for y in range(n):
        if graph[y][x] == 1:
            dfs(x, y)
            count_list.append(count)
            count = 0

count_list.sort()
print(len(count_list))
for cnt in count_list:
    print(cnt)