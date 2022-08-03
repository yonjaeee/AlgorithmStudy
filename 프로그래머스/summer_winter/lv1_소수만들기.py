import math
from itertools import combinations

def solution(nums):
    nums.sort(reverse = True)
    max_sum = sum(nums[:3])
    com_list = combinations(nums, 3)
    sum_list = [sum(x) for x in com_list]
    prime_list = [2, 3]
    for i in range(5, max_sum+1):
        prime = True
        for j in prime_list:
            if i % j == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(i)
    answer = 0
    for a in sum_list:
        if a in prime_list:
            answer += 1
    return answer