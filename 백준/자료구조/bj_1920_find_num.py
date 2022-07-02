# 이분 탐색 이용
import sys

def binary_search(target, data):
  start = 0
  end = len(data) - 1
  while start <= end:
    mid = (start + end) // 2
    if data[mid] == target:
      return 1
    elif data[mid] < target:
      start = mid + 1
    else:
      end = mid - 1

  return 0

N = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().strip().split()))
for num in m_list:
  print(binary_search(num, n_list))