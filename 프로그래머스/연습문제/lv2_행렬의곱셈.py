def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        layer = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            layer.append(temp)
        answer.append(layer)
    return answer