def solution(num):
    answer = 0
    if num == 0:
        return 0
    while answer <= 500:
        if num == 1:
            return answer
        if num % 2 == 0:
            num = num // 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1
    return -1