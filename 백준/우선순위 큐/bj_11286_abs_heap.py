# 시간 초과
'''
N = int(sys.stdin.readline())
arr = []
abs_arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        arr.append(x)
        heapq.heappush(abs_arr, abs(x))
    elif x == 0:
        if len(abs_arr) > 0:
            abs_num = heapq.heappop(abs_arr)
            if -1 * abs_num in arr:
                arr.remove(-1 * abs_num)
                print(-1 * abs_num)
            else:
                arr.remove(abs_num)
                print(abs_num)
        else:
            print(0)
'''
# 튜플 사용
import sys
import heapq

arr = [] 
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if len(arr) > 0:
            print(heapq.heappop(arr)[1])
        else:
            print(0)