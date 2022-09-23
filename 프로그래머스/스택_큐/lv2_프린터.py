# enumerate 사용하여 위치 저장
# 대기목록 순서를 모두 찾지 말고
# location에 있는 것 까지만

from collections import deque

def solution(priorities, location):
    answer = 0
    sorted_pr = sorted(priorities, reverse = True)
    pr_idx = 0
    queue = deque(enumerate(priorities))
    while queue:
        doc = queue.popleft()
        if doc[1] == sorted_pr[pr_idx]:
            pr_idx += 1
            if doc[0] == location:
                return pr_idx
        else:
            queue.append(doc)  