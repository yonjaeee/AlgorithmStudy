import sys

n, m = map(int, sys.stdin.readline().strip().split())
mil_list = list()
for i in range(n):
    p, l = map(int, sys.stdin.readline().strip().split())
    mil = list(map(int, sys.stdin.readline().strip().split()))
    if p < l:
        mil_list.append(1)
    else:
        mil.sort(reverse = True)
        mil_list.append(mil[l-1])
mil_list.sort()
num = 0
for i in range(n):
    m -= mil_list[i]
    if m < 0:
        break
    else:
        num += 1
# print(num)을 for문 안에 넣으면 마일리지 남는 경우 print 안됨
print(num)