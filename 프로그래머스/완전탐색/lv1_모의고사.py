def solution(answers):
    q_num = len(answers)
    score1 = 0
    score2 = 0
    score3 = 0
    
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(q_num):
        a = i % 5
        b = i % 8
        c = i % 10
        if answers[i] == a + 1:
            score1 += 1
        if answers[i] == second[b]:
            score2 += 1
        if answers[i] == third[c]:
            score3 += 1
        scores = [score1, score2, score3]
        m = max(scores)
        # enumerate 활용하기
        answer = [i+1 for i, v in enumerate(scores) if v == m]
    return answer