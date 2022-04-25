# 올림할 때 math.ceil() 함수 사용하기
# 개인 함수 만들다 틀릴 수 있음

from collections import deque
import math

def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    queue = deque(days)
    answer = []
    num = 0
    maxi = 0
    for j in range(len(days)):
        a = queue.popleft()
        if a <= maxi:
            num += 1
        else:
            answer.append(num)
            maxi = a
            num = 1
    if num != 0:
        answer.append(num)
    answer = answer[1:]
    return answer