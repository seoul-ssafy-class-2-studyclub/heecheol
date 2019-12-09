import collections
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
queue = collections.deque([N])
time = 0
flag = False
while queue:
    K += time
    if K > 500000:
        break

    visit = [0] * 500001
    for i in range(len(queue)):
        cur = queue.popleft()

        if cur == K:
            flag = True
            break

        if cur >= 1 and visit[cur - 1] == 0:
            visit[cur - 1] = 1
            queue.append(cur - 1)

        if cur <= 499999 and visit[cur + 1] == 0:
            visit[cur + 1] = 1
            queue.append(cur + 1)

        if cur <= 250000 and visit[2 * cur] == 0:
            visit[2 * cur] = 1
            queue.append(2 * cur)

    if flag is True:
        break

    time += 1

if flag is True:
    print(time)
else:
    print(-1)
