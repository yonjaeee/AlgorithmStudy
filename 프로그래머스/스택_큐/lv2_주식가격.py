# cnt 어떻게 증가시킬지 주의
# 그냥 중첩 for문으로 풀었는데 어떻게 하면 더 효율적일지 고민 필요

from collections import deque

def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i, len(prices)-1):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                break
        answer.append(cnt)
    return answer