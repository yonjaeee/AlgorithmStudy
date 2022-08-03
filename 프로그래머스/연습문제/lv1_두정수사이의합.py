def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif a < b:
        answer = sum(range(a, b+1))
    else:
        answer = sum(range(a, b-1, -1))
    return answer