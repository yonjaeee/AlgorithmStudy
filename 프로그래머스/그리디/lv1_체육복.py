# n = 3, lost = [1, 2], reserve = [2, 3]
# 반례 고려하기

def solution(n, lost, reserve):
    lost_ = set(lost)
    reserve_ = set(reserve)
    both = (lost_ & reserve_)
    for i in both:
        lost.remove(i)
        reserve.remove(i)
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    for r in reserve:
        if r in lost:
            lost.remove(r)
            answer += 1
        elif r-1 in lost:
            lost.remove(r-1)
            answer += 1
        elif r+1 in lost:
            lost.remove(r+1)
            answer += 1
    return answer