def solution(sizes):
    sizes_wh = [[max(w, h), min(w, h)] for [w, h] in sizes]
    w = [w for [w, h] in sizes_wh]
    h = [h for [w, h] in sizes_wh]
    answer = max(w) * max(h)
    return answer