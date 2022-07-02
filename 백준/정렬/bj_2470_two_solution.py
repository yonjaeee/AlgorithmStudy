import sys
import heapq

N = int(sys.stdin.readline())
sol_list = list(map(int, sys.stdin.readline().strip().split()))
sol = [(abs(i), i) for i in sol_list]
sol.sort()

mini = -1
for n in range(N-1):
    poss = abs(sol[n][1] + sol[n+1][1]) 
    if mini == -1:
        mini = poss
        result = sorted([sol[n][1], sol[n+1][1]])
    elif poss < mini:
        mini = poss
        result = sorted([sol[n][1], sol[n+1][1]])

print(result[0], result[1]) 