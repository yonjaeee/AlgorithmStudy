from collections import deque 

def solution(order):
    sub = []
    answer = 0
    n = len(order)
    maxi = 0
    cont = deque(range(1, n+1))
    for i in range(len(order)):
        if maxi > order[i]:
            if sub[-1] != order[i]:
                break
            else:
                answer += 1
                sub.pop()
        else:
            while True:
                try:
                    temp = cont.popleft()
                    maxi = temp
                    if temp == order[i]:
                        answer += 1
                        break
                    else:
                        sub.append(temp)
                except:
                    break
    return answer
