import sys
from itertools import combinations
while True:
    test_case= list(map(int, sys.stdin.readline().strip().split()))
    k = test_case[0]
    if k == 0:
        break
    else:
        S = sorted(test_case[1:])
        comb = list(combinations(S, 6))
        for i in comb:
            print(i[0], i[1], i[2], i[3], i[4], i[5])
        print()