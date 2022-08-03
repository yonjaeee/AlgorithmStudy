def solution(phone_number):
    phone_len = len(phone_number)
    answer = '*' * (phone_len-4) + phone_number[phone_len-4:]
    return answer