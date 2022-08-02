from itertools import combinations

def solution(number):
    three_nums = combinations(number, 3)
    three_nums_sum = [sum(x) for x in three_nums]
    return three_nums_sum.count(0)