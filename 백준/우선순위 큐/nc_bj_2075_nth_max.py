import sys
import heapq

N = int(sys.stdin.readline())
for i in range(N):
    each_row = list(map(int, sys.stdin.readline().strip().split()))
    # 한 column 별로 sort? array 만든다음 전체 처리?