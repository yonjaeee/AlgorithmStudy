# i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
# max_value d[i]로 업데이트 하는 것 잊지 말기

import sys

N = int(sys.stdin.readline())
t = []
p = []
d = [0] * (N+1)
max_value = 0
for i in range(N):
  t_, p_ = map(int, sys.stdin.readline().strip().split())
  t.append(t_)
  p.append(p_)
for i in range(N-1, -1, -1):
  time = t[i] + i
  if time > N:
    d[i] = max_value
  else:
    d[i] = max(d[time] + p[i], max_value)
    max_value = d[i]
print(d[0])