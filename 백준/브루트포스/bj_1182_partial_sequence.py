import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0
# range(1, n+1)인 것 주의
for n_ in range(1, n+1):
    com = combinations(num_list, n_)
    sum_list = [sum(com_) for com_ in com]
    cnt += sum_list.count(s)
print(cnt)