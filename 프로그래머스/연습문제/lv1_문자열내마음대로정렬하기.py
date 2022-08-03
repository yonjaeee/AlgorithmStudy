# 처음에 sort하고 이후에 조건을 걸어야 사전순대로 배열

def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda x: x[n])
    return strings