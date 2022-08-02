from collections import Counter, deque
def solution(want, number, discount):
    d_num = Counter(discount)
    curr_want = dict(zip(want, number))
    for c in curr_want.keys():
        if c not in d_num:
            return 0
        elif d_num[c] < curr_want[c]:
            return 0
    answer = 0
    for i in range(len(discount)-9):
        if curr_want == Counter(discount[i:i+10]):
            answer += 1
    return answer
