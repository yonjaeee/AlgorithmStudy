# 인형 뽑고나서 뽑은 자리 초기화 안해줬음

def solution(board, moves):
    n = len(board)
    dolls = []
    answer = 0
    for move in moves:
        for i in range(n):
            if board[i][move-1] != 0:
                doll = board[i][move-1]
                board[i][move-1] = 0
                if len(dolls) == 0:
                    dolls.append(doll)
                elif doll == dolls[-1]:
                    dolls.pop()
                    answer += 2
                else:
                    dolls.append(doll)
                break
    return answer