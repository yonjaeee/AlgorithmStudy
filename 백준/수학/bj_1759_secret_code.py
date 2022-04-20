# itertools.combinations 사용
from itertools import combinations
import sys

# 정수로 받는거 잊지 않가
# 최소 한 개의 모음과 최소 두 개의 자음 조건
l, c = map(int, sys.stdin.readline().strip().split())
letter_list = sys.stdin.readline().strip().split()
letter_list.sort()
aeiou_list = ['a', 'e', 'i', 'o', 'u']
for i in combinations(letter_list, l):
    aeiou_num = 0
    for a in aeiou_list:
        if a in i:
            aeiou_num += 1
    if aeiou_num < 1 or aeiou_num > l - 2:
        pass
    else:
        string = ''
        for j in i:
            string += j
        print(string)