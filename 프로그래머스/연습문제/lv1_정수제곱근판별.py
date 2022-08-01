import math

def solution(n):
    if math.sqrt(n) - int(math.sqrt(n)) > 0:
        return -1
    else:
        x = int(math.sqrt(n))
        return (x+1) ** 2