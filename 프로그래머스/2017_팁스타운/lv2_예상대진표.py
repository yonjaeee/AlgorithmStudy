def solution(n,a,b):
    answer = 1
    big = max(a, b)
    small = min(a, b)
    while True:
        if (big // 2) - (small // 2) == 1 and big % 2 == 0 and small % 2 == 1:
            break
        else:
            big = (big + 1) // 2
            small = (small + 1) // 2
            answer += 1
    return answer