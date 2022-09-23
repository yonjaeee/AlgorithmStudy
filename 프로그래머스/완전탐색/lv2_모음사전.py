from itertools import product

def solution(word):
    vowels = 'AEIOU'
    word_list = ['A', 'E', 'I', 'O', 'U']
    for i in range(2, 6):
        for j in product(vowels, repeat = i):
            word_list.append(''.join(j))
    word_list.sort()
    answer = word_list.index(word) + 1
    return answer