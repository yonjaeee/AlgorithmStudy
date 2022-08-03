def solution(x):
    x_str = str(x)
    x_list = list(x_str)
    x_list = map(int, x_list)
    div = sum(x_list)
    if x % div == 0:
        return True
    else:
        return False