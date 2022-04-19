import sys

s = set()
M = int(sys.stdin.readline())
for _ in range(M):
    # strip해서 에러 막기
    func_num = sys.stdin.readline().strip().split()
    # func_num은 리스트형 -> str형으로 바꿔줘야 함
    if len(func_num) == 1:
        func = func_num[0]
        if func == 'all':
            s.update([x for x in range(1, 21)])
        elif func == 'empty':
            s.clear()
    else:
        func = func_num[0]
        num = int(func_num[1])
        if func == 'add':
            s.add(num)
        elif func == 'remove':
            s.discard(num)
        elif func == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif func == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)