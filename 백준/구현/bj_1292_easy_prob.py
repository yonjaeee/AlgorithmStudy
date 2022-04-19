import sys
start, end = map(int, sys.stdin.readline().strip().split())
# 그냥 단순 구현이 편할 때도 있다
nums = [0]
for i in range(1, 50):
    for j in range(i): 
        nums.append(i)
print(sum(nums[start:end+1]))



