# 햄버거 문제
def solution(ingredient):
    answer = 0
    end_pointer = 4
    if len(ingredient) < 4:
        return 0
    else:
        while end_pointer <= len(ingredient):
            if ingredient[end_pointer-4:end_pointer] == [1, 2, 3, 1]:
                del ingredient[end_pointer-4:end_pointer]
                answer += 1
                end_pointer -= 3
            else:
                end_pointer += 1
    return answer