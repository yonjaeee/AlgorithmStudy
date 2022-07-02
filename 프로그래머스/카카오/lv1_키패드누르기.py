def solution(numbers, hand):
    answer = []
    l = 3
    r = 3
    pr = 1
    pl = 1
    if hand == "right":
        hand = 'R'
    else:
        hand = 'L'
        
    for i in range(len(numbers)):
        if int(numbers[i]) in [1, 4, 7]:
            answer.append('L')
            l = numbers[i]//3
            pl = 1
        elif int(numbers[i]) in [3, 6, 9]:
            answer.append('R')
            r = (numbers[i]//3)-1
            pr = 1
        elif int(numbers[i]) in [2, 5, 8]:
            c = numbers[i]//3
            if abs(l-c)+pl > abs(r-c)+pr:
                answer.append('R')
                r = numbers[i]//3
                pr = 0
            elif abs(l-c)+pl < abs(r-c)+pr:
                answer.append('L')
                l = numbers[i]//3
                pl = 0
            else:
                answer.append(hand)
                if hand == 'R':
                    r = numbers[i]//3
                    pr = 0
                else:
                    l = numbers[i]//3
                    pl = 0
        else:
            if (3-l)+pl > (3-r)+pr:
                answer.append('R')
                r = 3
                pr = 0
            elif (3-l)+pl < (3-r)+pr:
                answer.append('L')
                l = 3
                pl = 0
            else:
                answer.append(hand)
                if hand == 'R':
                    r = 3
                    pr = 0
                else:
                    l = 3
                    pl = 0
    answer = ''.join(answer)
    
    return answer