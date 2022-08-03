def solution(arr):
    if len(arr) == 0:
        return [-1]
    else:
        arr.remove(min(arr))
        if len(arr) == 0:
            arr = [-1]
        return arr