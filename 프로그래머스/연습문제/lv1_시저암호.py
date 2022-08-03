def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif ord('a') <= ord(s[i]) <= ord('z'):
            if ord(s[i]) + n <= ord('z'):
                answer += chr(ord(s[i]) + n)
            else:
                answer += chr(ord(s[i]) + n - 1 - ord('z') + ord('a'))
        else:
            if ord(s[i]) + n <= ord('Z'):
                answer += chr(ord(s[i]) + n)
            else:
                answer += chr(ord(s[i]) + n - 1 - ord('Z') + ord('A'))
    return answer