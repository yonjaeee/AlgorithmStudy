p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

vec12 = [p2[0]-p1[0], p2[1]-p1[1]]
vec23 = [p3[0]-p2[0], p3[1]-p2[1]]

if vec12[0] == 0 and vec23[0] == 0:
    print(0)
elif vec12[1] == 0 and vec23[1] == 0:
    print(0)
elif vec12[0] != 0 and vec12[1] != 0:
    if vec23[0] / vec12[0] == vec23[1] / vec12[1]:
        print(0)
        