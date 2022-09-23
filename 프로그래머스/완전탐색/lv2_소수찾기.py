# 에라토스테네스의 체 
from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    num_list = list(numbers)
    created_list = []
    for i in range(1, len(numbers)+1):
        temp_list = permutations(num_list, i)
        temp_list = [int(''.join(x)) for x in temp_list]
        created_list.extend(temp_list)
    created_list.sort()
    created_list = list(set(created_list))
    answer = 0
    for i in range(len(created_list)):
        if is_prime(created_list[i]):
            answer += 1
    return answer