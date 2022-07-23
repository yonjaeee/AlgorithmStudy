# 처음에는 문자열 길이로 정렬했으나 효율성 테스트 통과 안됨
# 문자열 sort 후, 조건 걸기
def solution(phone_book):
    answer = True
    phone_dict = dict()
    phone_book.sort()
    br = False
    for i in range(len(phone_book)):
        if i == 0:
            phone_dict[phone_book[i]] = True
        elif len(phone_book[i]) < len(phone_book[i-1]):
            phone_dict[phone_book[i]] = True
        else:
            for j in range(1, len(phone_book[i])):
                if phone_dict.get(phone_book[i][:j]) != None:
                    answer = False
                    br = True
                    break
            phone_dict[phone_book[i]] = True 
        if br == True:
            break
        
    return answer