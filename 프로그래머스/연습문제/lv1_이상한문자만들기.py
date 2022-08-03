def solution(s):
    ans_list = []
    s = s.replace(' ', ' / ')
    s_list = s.split()
    for s_ in s_list:
        if s_ == '/':
            ans = ' '
        else:
            ans = ''
            for i in range(len(s_)):
                if i % 2 == 0:
                    ans += s_[i].upper()
                else:
                    ans += s_[i].lower()
        ans_list.append(ans)
    answer = ''.join(ans_list)
    return answer