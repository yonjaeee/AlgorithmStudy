# 리스트 컴프리헨션 사용
# Counter 사용

from collections import Counter

def solution(id_list, report, k):
    report = list(set(report))
    reported = list(map(lambda x: x.split()[1], report))
    reported_num = dict(Counter(reported))
    stopped = [key for key, value in reported_num.items() if value >= k]
    reporter = [x.split()[0] for x in report if x.split()[1] in stopped]
    answer = []
    for id in id_list:
        answer.append(reporter.count(id))
    return answer