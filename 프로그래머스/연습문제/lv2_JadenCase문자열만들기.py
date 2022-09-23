# 공백문자 연속해서 나오는 경우
def solution(s):
    capital = True
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            capital = True
            answer += ' '
        elif capital == True:
            answer += s[i].upper()
            capital = False
        else:
            answer += s[i].lower()
            capital = False
    return answer