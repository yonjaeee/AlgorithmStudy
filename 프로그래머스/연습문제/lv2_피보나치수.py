# 시간복잡도 생각한 풀이
# 1234567 나눈 나머지 빼먹지 말기
def solution(n):
    d = [0] * (n+1)
    d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n] % 1234567