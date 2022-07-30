# 첫집을 터는 경우와 아닌 경우로 나눈 후 최대값 구하기

def solution(money):
    N = len(money)
    dp1 = [0] * N    # 첫번째 집 터는 경우
    dp2 = [0] * N    # 첫번째 집 무시하는 경우
    for i in range(N):
        if i == 0:
            dp1[i] = money[i]
        elif 1 <= i < N-1:
            dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    answer = max(dp1[N-2], dp2[N-1])
    return answer