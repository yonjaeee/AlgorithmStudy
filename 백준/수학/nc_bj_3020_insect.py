# 메모리 초과
import sys

N, H = map(int, sys.stdin.readline().strip().split())
total_obs = []
for i in range(N):
    height = int(sys.stdin.readline())
    obs = [0 for _ in range(H)]
    if i % 2 == 0:
        for j in range(1, height+1):
            obs[-j] = 1
    else:
        for j in range(height):
            obs[j] = 1
    total_obs.append(obs)

answer = N
answer_num = 1
for h in range(H):
    obs_num = 0
    for i in range(N):
        obs_num += total_obs[i][h]
    if obs_num < answer:
        answer = obs_num
        answer_num = 1
    elif obs_num == answer:
        answer_num += 1
print(answer, answer_num)
