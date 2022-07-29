# 처음엔 for문이 중첩되서 도는게 싫어서 maximum, idx 등 이용하여 구하려 했음
# 그러면 앞 수보다 큰 값을 제거하기만 하는 알고리즘이 됨
# 가장 긴 증가하는 부분 수열을 만들어야 하므로 DP가 필요
# 중간에 갑자기 커지는 숫자가 있으면 그 숫자를 제거하는 게 좋듯 여러 상황이 있음
# 마지막을 d[N-1]로 하면 d[N-1]이 작은 수일 경우 고려 못함

import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
d = [1] * N

for i in range(1, N):
  for j in range(0, i):
    if a[i] > a[j]:
      d[i] = max(d[i], d[j] + 1)
print(max(d))