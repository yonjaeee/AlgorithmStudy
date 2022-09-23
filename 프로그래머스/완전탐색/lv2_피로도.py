# 던전 개수가 작음에 따라 완전탐색 가능하다고 생각 가능
# 다른 방식으로(그리디, 정렬) 했을 때는 고려 못하는 사항들 있음

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons.sort(key = lambda x: (-x[1], x[0]))
    order_list = list(permutations(dungeons))
    for i in range(len(order_list)):
        hit = 0
        hp = k
        order = order_list[i]
        for j in range(len(order)):
            if hp >= order[j][0]:
                hp -= order[j][1]
                if hp > 0:
                    hit += 1
                else:
                    break
            else:
                break
        if hit > answer:
            answer = hit
    return answer