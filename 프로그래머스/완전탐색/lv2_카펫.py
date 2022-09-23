def solution(brown, yellow):
    for height in range(1, brown // 4 + 2):
        if (brown + yellow) % height == 0:
            width = (brown + yellow) // height
            if ((width - 2) * (height - 2) == yellow) & ((width + height - 2) * 2 == brown):
                return [width, height]