import sys
from itertools import accumulate

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
sum_nums = list(accumulate(nums))
for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    if i == j:
        print(nums[i-1])
    elif i == 1:
        print(sum_nums[j-1])
    else:
        print(sum_nums[j-1] - sum_nums[i-2])