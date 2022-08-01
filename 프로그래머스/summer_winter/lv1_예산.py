def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget > 0:
            answer += 1
        elif budget == 0:
            answer += 1
            break
        else:
            break
    return answer