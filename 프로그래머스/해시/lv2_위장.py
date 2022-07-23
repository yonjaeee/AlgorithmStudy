def solution(clothes):
    cloth_dict = dict()
    for cloth in clothes:
        name, cat = cloth
        if cat not in cloth_dict:
            cloth_dict[cat] = 1
        else:
            cloth_dict[cat] += 1
    nums = cloth_dict.values()
    answer = 1
    for num in nums:
        answer *= (num + 1)
    answer -= 1
    return answer