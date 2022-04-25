# 처음엔 효율성 테스트 통과 못함
# list에 in으로 일일이 확인 했었음

from collections import Counter

def solution(participant, completion):
    # 동명이인 아닌 사람이 complete 하지 못하였을 때
    par_set = set(participant)
    comp_set = set(completion)
    if len(par_set - comp_set) == 1:
        return list(par_set - comp_set)[0]
    # 동명이인인 사람이 complete 하지 못하였을 때
    else:
        par_cnt = dict(Counter(participant))
        comp_cnt = dict(Counter(completion))
        for comp in list(comp_cnt.keys()):
            if par_cnt[comp] != comp_cnt[comp]:
                return comp