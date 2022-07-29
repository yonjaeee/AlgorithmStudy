# 최소값이 8 이하인 결과값을 미리 만들어놓기
# 5 = 5 = 4+1 = 3+2 = 2+3 = 1+4
# 집합 8개 만들어 처리


def solution(N, number):
    cal_list = [set() for x in range(9)]
    cal_list[1] = {N}
    if number == N:
        return 1
    else:
        for i in range(2, 9):
            basic_num = int(str(N) * i)
            cal_list[i].add(basic_num)
            for j in range(1, i):
                for num1 in cal_list[j]:
                    for num2 in cal_list[i-j]:
                        cal_list[i].add(num1 + num2)
                        cal_list[i].add(num1 - num2)
                        cal_list[i].add(num1 * num2)
                        if num2 != 0:
                            cal_list[i].add(num1 // num2)
            if number in cal_list[i]:
                return i
    return -1