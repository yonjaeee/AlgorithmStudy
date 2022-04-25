# 시간초과
# 매번 뒤집지 않고, reverse 연속으로 나온 횟수 세기

import sys
from collections import deque

T = int(sys.stdin.readline())

def ac(string, num_list):
    num_q = deque(num_list)
    reverse = 0
    for i in range(len(string)):
        if string[i] == 'R':
            reverse += 1
        elif len(num_q) == 0:
            return 'error'
        else:
            if reverse % 2 == 0:
                reverse = 0
                num_q.popleft()
            else:
                num_q.reverse()
                reverse = 0
                num_q.popleft()

    return list(num_q)

for t in range(T):
    string_ = sys.stdin.readline().strip()
    num_ = int(sys.stdin.readline().strip())
    num_string_ = sys.stdin.readline().strip()
    if num_ > 0:
        num_list_ = list(map(int, num_string_[1:-1].split(',')))
        print(ac(string_, num_list_))
    else:
        print(ac(string_, []))