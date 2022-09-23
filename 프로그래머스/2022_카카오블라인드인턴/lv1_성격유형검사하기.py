# 문제 조건 제대로 읽기
def solution(survey, choices):
    answer = ''
    order_alpha = ['RT', 'CF', 'JM', 'AN']
    score_dict = {'R': 0, 'T': 0, 'F': 0, 'C': 0, 'M': 0, 'J': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        choice = choices[i]
        option = survey[i]
        if choice == 4:
            pass
        elif choice < 4:
            score_dict[option[0]] += (4 - choice)
        else:
            score_dict[option[1]] += (choice - 4)
    for j in range(len(order_alpha)):
        if score_dict[order_alpha[j][0]] >= score_dict[order_alpha[j][1]]:
            answer += order_alpha[j][0]
        else:
            answer += order_alpha[j][1]
    return answer