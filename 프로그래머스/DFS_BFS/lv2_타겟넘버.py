# dfs/bfs 문제라고 해서 기존의 틀대로 풀어야 한다는 강박이 있던 것 같다
# 일단 문제를 보고 떠오르는대로 푸는 게 중요

def solution(numbers, target):
    answer = 0
    before_list = []
    after_list = []
    for num in numbers:
        before_list = after_list
        after_list = []
        if len(before_list) == 0:
            after_list.append(num)
            after_list.append(-num)
        else:
            # range 안써서 틀렸었음
            for _ in range(len(before_list)):
                temp = before_list.pop()
                after_list.append(temp + num)
                after_list.append(temp - num)
    for a in after_list:
        if a == target:
            answer += 1
    return answer