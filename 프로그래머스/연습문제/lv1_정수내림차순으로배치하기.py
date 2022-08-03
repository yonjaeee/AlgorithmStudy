def solution(n):
    num_list = list(str(n))
    num_list.sort(reverse = True)
    answer = int(''.join(num_list))
    return answer