def solution(n, m):
    if m == n: 
        return [m, n]
    else:
        sub = abs(m-n)
        for i in range(sub, 0, -1):
            if (n % i == 0) and (m % i == 0):
                return [i, m*n//i]