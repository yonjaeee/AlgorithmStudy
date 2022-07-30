# 0XXXXX 값을 위하여 밑의 과정 삽입
# but test case 1-6 메모리 + 시간 너무 많이 써서 실패

def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(reverse = True)
    for i in range(len(str_numbers) - 1):
        if str_numbers[i][0] == str_numbers[i+1][0]:
            if len(str_numbers[i]) != len(str_numbers[i+1]):
                now_num = int(str_numbers[i] + str_numbers[i+1])
                rev_num = int(str_numbers[i+1] + str_numbers[i])
                if rev_num > now_num:
                    temp = str_numbers[i]
                    str_numbers[i] = str_numbers[i+1]
                    str_numbers[i+1] = temp
    answer = ''.join(str_numbers)
    answer = str(int(answer))
    return answer

# numbers의 원소가 0이상 1000이하라는 것에서 착안

def solution_real(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key = lambda x: x*3, reverse = True)
    answer = ''.join(str_numbers)
    answer = str(int(answer))
    return answer