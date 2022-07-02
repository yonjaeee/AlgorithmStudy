# 양수, 음수, 0일 때 case by case 접근
# 양수일 때는 큰거 끼리 곱하고 마지막 남은건 그냥 더해주기
# 음수일 때는 작은거 끼리 곱하고 마지막 남은건 0이 있다면 양수로 만들어주기

import sys

N = int(sys.stdin.readline())
pos_list = []
zero_list = []
neg_list = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        pos_list.append(num)
    elif num == 0:
        zero_list.append(num)
    else:
        neg_list.append(num)
pos_list.sort(reverse = True)
neg_list.sort()
result = 0

while True:
    if len(pos_list) >= 2:
        if pos_list[1] > 1:
            result += pos_list[0] * pos_list[1]
        # 2, 1 이런 식으로 나오면 따로 따로 더하는 게 나
        else:
            result += (pos_list[0] + pos_list[1])
        del pos_list[0]
        del pos_list[0]
    elif len(pos_list) == 1:
        result += pos_list[0]
        del pos_list[0]
        break
    else:
        break

while True:
    if len(neg_list) >= 2:
        result += neg_list[0] * neg_list[1]
        del neg_list[0]
        del neg_list[0]
    elif len(neg_list) == 1:
        if len(zero_list) == 0:
            result += neg_list[0]
        del neg_list[0]
        break
    else:
        break

print(result)