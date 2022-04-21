def solution(nums):
    N = len(nums)
    nums_set = set(nums)
    if len(nums_set) > N/2:
        answer = int(N/2)
    else:
        answer = len(nums_set)
        
    return answer