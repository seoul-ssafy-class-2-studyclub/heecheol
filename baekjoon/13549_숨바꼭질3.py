import sys
sys.stdin = open('input.txt', 'r')
import collections

N, K = map(int, input().split())
queue = collections.deque([N])
time = 0
flag = False
visit = [0] * 100001
visit[N] = 1

while queue:
    for i in range(len(queue)):
        c = queue.popleft()
        queue.append(c)
        c *= 2
        while 0 < c <= 100000:
            if visit[c] is 0:
                visit[c] = 1
                queue.append(c)
            c *= 2

    for i in range(len(queue)):
        cur = queue.popleft()
        if cur == K:
            flag = True
            break

        nxts = [cur - 1, cur + 1]
        for nxt in nxts:
            if 0 <= nxt <= 100000 and visit[nxt] is 0:
                queue.append(nxt)
                visit[nxt] = 1

    if flag is True:
        break
    time += 1

print(time)
