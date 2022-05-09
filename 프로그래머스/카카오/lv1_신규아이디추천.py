import re

# 정규표현식에 대한 이해 필요

def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = re.sub('[^0-9a-z_.\-]+', "", answer)
    # 3단계
    # 이 파트 중요
    answer = re.sub("\.\.+", ".", answer)
    # 4단계
    # strip 이용하여 공백 제거 뿐 아니라 원하는 문자 제거 가능
    answer = answer.strip('.')
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]
    # 7단계
    if len(answer) <= 2:
        # while은 반복문 돌아가는 조건 써놔야함
        while len(answer) != 3:
            answer += answer[-1]
    return answer