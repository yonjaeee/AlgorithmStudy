import sys
from collections import deque

T = int(sys.stdin.readline())

def ac(string, num_list):
    num_q = deque(num_list)
    for i in range(len(string)):
        if string[i] == 'R':
            num_q.reverse()
        elif len(num_q) == 0:
            return 'error'
        else:
            num_q.popleft()
    return list(num_q)

for t in range(T):
    string_ = sys.stdin.readline().strip()
    num_ = int(sys.stdin.readline().strip())
    num_string_ = sys.stdin.readline().strip()
    if num_ == 0:
        print('error')
    else:
        num_list_ = list(map(int, num_string_[1:-1].split(',')))
        print(ac(string_, num_list_))