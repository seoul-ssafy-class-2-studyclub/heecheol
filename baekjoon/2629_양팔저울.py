import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
scales = list(map(int, input().split()))
visit = [False] * 80001

weight = [40000]
for i in range(N):
    scale = scales[i]
    for j in range(len(weight)):
        left = weight[j] - scale
        if visit[left] is False:
            visit[left] = True
            weight.append(left)

        right = weight[j] + scale
        if visit[right] is False:
            visit[right] = True
            weight.append(right)

M = int(input())
balls = list(map(int, input().split()))
answer = ['-'] * M
for i in range(M):
    if visit[balls[i] + 40000] is True:
        answer[i] = 'Y'
    else:
        answer[i] = 'N'

print(' '.join(answer))
