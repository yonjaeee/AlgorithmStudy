def solution(absolutes, signs):
    real = list()
    for i in range(len(signs)):
        if signs[i] == True:
            real.append(absolutes[i])
        else:
            real.append(-1 * absolutes[i])
    answer = sum(real)
    return answer