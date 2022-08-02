# set 함수가 시간복잡도에 있어 비싼 함수

from collections import deque, Counter

def solution(topping):
    types = len(set(topping))
    length = len(topping)
    if length == 1:
        return 0
    elif types == 1:
        return length-1
    else:
        answer = 0
        l1 = topping[:(types-1)//2]
        l2 = deque(topping[(types-1)//2:])
        c1 = Counter(l1)
        c2 = Counter(l2)
        n1 = len(set(l1))
        n2 = len(set(l2))
        for i in range((types+1)//2, length-(types-1)//2):
            temp = l2.popleft()
            c2[temp] -= 1
            if c2[temp] == 0:
                n2 -= 1
            if temp not in c1:
                c1[temp] = 1
                n1 += 1
            if n1 == n2:
                answer += 1
            elif n1 > n2:
                break
    return answer

'''
        for i in range((types+1)//2, length-(types-1)//2):
            l1 = topping[:i]
            set1 = set(l1)
            l2 = topping[i:]
            set2 = set(l2)
            if len(set1) == len(set2):
                answer += 1
            elif answer != 0:
                break'''