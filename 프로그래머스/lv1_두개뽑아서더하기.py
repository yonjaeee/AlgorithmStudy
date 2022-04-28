from itertools import combinations

def solution(numbers):
    two_list = list(combinations(numbers, 2))
    sum_list = [x+y for x, y in two_list]
    answer = list(set(sum_list))
    # set 거쳤다고 sort 안하면 에러남
    answer.sort()
    return answer