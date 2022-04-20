# 시간 초과
"""import sys
N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline())

for i in range(1, num_list[-1]):
    new_num_set = set([x%i for x in num_list])
    if len(new_num_set) == 1:
        print(i, end = " ")"""
import math
import sys
N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    # int형 주의
    num_list.append(int(sys.stdin.readline()))
sub_num_list = []
for i in range(N-1):
    sub_num_list.append(num_list[i+1] - num_list[i])
for i in range(min(sub_num_list), 1, -1):
    div = sub_num_list[0] % i
    for j in range(1, N-1):
        if sub_num_list[j] % i != div:
            div = -1
            break
    if div >= 0:
        maxi = i
        break
div_set = set()
for i in range(int(math.sqrt(maxi))):
    if maxi % i == 0:
        div_set.add(i)
        div_set.add(int(maxi / i))
div_set.remove(1)
for i in div_set:
    print(i, end = " ")

