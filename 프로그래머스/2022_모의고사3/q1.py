# 콜라 문제
def solution(a, b, n):
    answer = 0
    left = n
    while left >= a:
        div = left // a
        remain = left % a
        left = div * b + remain
        answer += div * b
    return answer