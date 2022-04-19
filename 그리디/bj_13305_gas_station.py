import sys

N = int(sys.stdin.readline())
road_lst = list(map(int, sys.stdin.readline().split()))
gas_lst = list(map(int, sys.stdin.readline().split()))

curr_idx = 0
total = 0
for i in range(1, N):
    total += gas_lst[curr_idx] * road_lst[i-1] 
    if gas_lst[i] < gas_lst[curr_idx]:
        curr_idx = i
print(total)
