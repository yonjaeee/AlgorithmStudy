# 과거 길찾기 문제의 알고리즘을 생각
# 다 1을 배정해놓고 물구덩이 생긴 곳만 0으로 처리
# index -1도 찾을 수 있으므로 예외 처리

def solution(m, n, puddles):
    d = [[1] * n for x in range(m)]
    for i in range(m):
        for j in range(n):
            if [i+1, j+1] in puddles:
                d[i][j] = 0
            elif i == 0 and j == 0:
                pass
            elif i == 0:
                d[i][j] = d[i][j-1]
            elif j == 0:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = d[i-1][j] + d[i][j-1]
    answer = d[m-1][n-1] % 1000000007
    return answer