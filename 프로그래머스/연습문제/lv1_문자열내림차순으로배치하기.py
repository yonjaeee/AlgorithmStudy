def solution(s):
    s_list = list(s)
    s_list.sort(key = lambda x: -ord(x))
    answer = ''.join(s_list)
    return answer