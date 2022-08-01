import math

def solution(n):
    div = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            if n // i == i:
                pass
            else:
                div.append(n//i)
    answer = sum(div)
    return answer