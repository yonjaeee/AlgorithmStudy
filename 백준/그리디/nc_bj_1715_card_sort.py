# 시간 초과 에러
# 우선순위 힙 써야 한다고 함
import sys
N = int(sys.stdin.readline())
cards = list()
total = 0
for _ in range(N):
    cards.append(int(sys.stdin.readline()))
if len(cards) == 1:
    total += cards[0]
while len(cards) >= 2:
    cards.sort()
    min1 = cards.pop(0)
    min2 = cards.pop(0)
    total += min1 + min2
    cards.append(min1 + min2)
print(total)