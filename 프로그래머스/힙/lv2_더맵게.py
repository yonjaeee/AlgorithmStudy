import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
            break
        else:
            mini1 = heapq.heappop(scoville)
            mini2 = heapq.heappop(scoville)
            heapq.heappush(scoville, mini1 + (mini2 * 2))
            answer += 1
    return answer