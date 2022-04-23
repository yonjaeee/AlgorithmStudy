# 어떤게 인덱스인지 어떤게 value인지 헷갈릴 수 있음

from collections import Counter
import heapq

def solution(N, stages):
    reached_players = len(stages)
    stages_cnt = dict(Counter(stages))
    answer = [0 for _ in range(N)]
    rates = []
    for i in range(1, N+1):
        if reached_players == 0:
            rates.append(0)
        else:
            now_players = stages_cnt.get(i, 0)
            rate = now_players / reached_players
            rates.append(rate)
            reached_players -= now_players
    enu_rates = [(-rate, idx+1) for idx, rate in enumerate(rates)]
    heapq.heapify(enu_rates)
    for i in range(N):
        rate_, idx_ = heapq.heappop(enu_rates)
        answer[i] = idx_
    return answer