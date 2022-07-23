# 아이디어 생각하기 어려웠음
# i의 R색으로 칠하는 최소비용은 i-1의 G와 B로 칠했을 때의 비용 중
# 최소의 비용을 더한 값
# bottom-up 방식(?)

import sys

N = int(sys.stdin.readline())
d = []
for i in range(N):
    d.append(list(map(int, sys.stdin.readline().strip().split())))
    if i > 0:
        d[i][0] += min(d[i-1][1], d[i-1][2])
        d[i][1] += min(d[i-1][0], d[i-1][2])
        d[i][2] += min(d[i-1][0], d[i-1][1])
print(min(d[N-1][0], d[N-1][1], d[N-1][2])) 