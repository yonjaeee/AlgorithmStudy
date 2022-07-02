# 뒷날부터 시작
# 각 날짜에 적립된 과제들 중 점수가 가장 큰 과제 선택
# 나머지 과제들을 앞의 날짜들에 적립

import sys
import heapq

N = int(sys.stdin.readline())
hw_list = [[] for x in range(1001)]
score_list = []
maxi_score = 0
for _ in range(N):
    d, w = map(int, sys.stdin.readline().strip().split())
    hw_list[d].append(w)

for i in range(1000, 0, -1):
    if len(score_list) == 0 and len(hw_list[i]) == 0:
        pass
    elif len(score_list) > 0 and len(hw_list[i]) == 0:
        maxi_score += heapq.heappop(score_list)[1]
    elif len(score_list) == 0 and len(hw_list[i]) > 0:
        for j in hw_list[i]:
            heapq.heappush(score_list, (-j, j))
        maxi_score += heapq.heappop(score_list)[1]
    else:
        for j in hw_list[i]:
            heapq.heappush(score_list, (-j, j))
        maxi_score += heapq.heappop(score_list)[1]
print(maxi_score)