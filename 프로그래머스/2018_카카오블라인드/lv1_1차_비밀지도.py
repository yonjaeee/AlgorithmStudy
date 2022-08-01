def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans = ''
        arr1_b = str(format(arr1[i], 'b'))
        arr2_b = str(format(arr2[i], 'b'))
        arr1_b = (n - len(arr1_b)) * '0' + arr1_b
        arr2_b = (n - len(arr2_b)) * '0' + arr2_b
        for j in range(n):
            if int(arr1_b[j]) + int(arr2_b[j]) >= 1:
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
    return answer