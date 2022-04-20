import math
from re import I
maxi, mini = map(int, input().strip().split())
other = int(mini / maxi)
divisor_list = list()
for x in range(int(math.sqrt(other)), 0, -1):
    if other % x == 0:
        # 여기에서도 최대공약수 문제
        divisor_list.append(x)
        divisor_list.append(int(other / x))
        break
divisor_list.sort()
print(maxi * divisor_list[0], maxi * divisor_list[1])

