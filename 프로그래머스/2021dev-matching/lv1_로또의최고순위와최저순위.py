def solution(lottos, win_nums):
    zero_cnt = 0
    ans_cnt = 0
    while 0 in lottos:
        lottos.remove(0)
        zero_cnt += 1
    for num in lottos:
        if num in win_nums:
            ans_cnt += 1
    max_cnt = ans_cnt + zero_cnt
    if ans_cnt < 2:
        ans_idx = 6
    else:
        ans_idx = 7 - ans_cnt
    if max_cnt < 2:
        max_idx = 6
    else:
        max_idx = 7 - max_cnt
    answer = [max_idx, ans_idx]
    return answer