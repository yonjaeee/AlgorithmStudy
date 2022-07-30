# 한명만 남았을 경우 고려하여 예외처리

from collections import deque

def solution(people, limit):
    people.sort(reverse = True)
    people = deque(people)
    answer = 0
    while len(people) > 0:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.popleft()
            try:
                people.pop()
            except:
                break
        else:
            answer += 1
            people.popleft()
    return answer