# n, times가 굉장히 클 수 있어 효율적인 알고리즘 필요
# 총 소요 시간을 변경시키며 사람수를 맞추자

def solution(n, times):
    answer = 0
    times.sort()
    start = times[0]
    end = times[0] * n
    while start <= end:
        ppl = 0
        mid = (start + end) // 2
        for time in times:
            ppl += mid // time
            if ppl >= n:
                break
        if ppl < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer