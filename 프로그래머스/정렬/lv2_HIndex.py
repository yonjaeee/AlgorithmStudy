# 처음에는 sort 한 다음 포인터를 움직여 조건 부합하여 cnt += 1
# 초기화를 다음 원소로 했었음
# 그 결과, 중간 숫자가 답일 경우 오답
# 이 방법은 문제 그대로 구현한 방법
# return len(citations) 하는 것 주의
# 오름차순이면 맨 아래에 return 0

def solution(citations):
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    return len(citations)