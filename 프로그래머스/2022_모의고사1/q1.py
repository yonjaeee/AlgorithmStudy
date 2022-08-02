from collections import Counter

def solution(X, Y):
    answer = ''
    x = Counter(list(X))
    y = Counter(list(Y))
    its = x & y
    its_sorted = sorted(its.items(), reverse = True)
    if len(its_sorted) == 0:
        return "-1"
    elif len(its_sorted) == 1 and its_sorted[0][0] == "0":
        return "0"
    else:
        for key, value in its_sorted:
            answer += key * value
        return answer
