def solution(n):
    k = n + 1
    n_binary = format(n, 'b')
    n_one_cnt = n_binary.count('1')
    while True:
        k_binary = format(k, 'b')
        k_one_cnt = k_binary.count('1')
        if k_one_cnt == n_one_cnt:
            break
        else:
            k += 1
    return k