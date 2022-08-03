def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    for i in s:
        if i in '1234567890':
            pass
        else:
            return False
    return True