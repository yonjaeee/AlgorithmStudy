def solution(array, commands):
    answer = []
    for l in range(len(commands)):
        i, j, k = commands[l]
        sliced_arr = array[i-1: j]
        sliced_arr.sort()
        ans = sliced_arr[k-1]
        answer.append(ans)
    return answer