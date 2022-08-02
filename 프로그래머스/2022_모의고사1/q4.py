def solution(beginning, target):
    changed = [[False] * len(beginning[0]) for x in range(len(beginning))]
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if beginning[i][j] != target[i][j]:
                changed[i][j] = True
    for i in range(len(changed)-1):
        if (changed[i] == changed[i+1]) or (changed[i] == [not c for c in changed[i+1]]):
            pass
        else:
            return -1
    changed_t = [[changed[i][j] for i in range(len(changed))] for j in range(len(changed[0]))]
    for i in range(len(changed_t)-1):
        if (changed_t[i] == changed_t[i+1]) or (changed_t[i] == [not c for c in changed_t[i+1]]):
            pass
        else:
            return -1
    column_changed = changed[0]
    cc = column_changed.count(True)
    row_changed = changed_t[0]
    rc = row_changed.count(True)
    if column_changed[0] == True:
        return min(cc + len(row_changed) - rc, len(column_changed) - cc + rc)
    else:
        return min(cc + rc, len(column_changed) - cc + len(row_changed) - rc)
