import sys
sys.stdin = open('input.txt', 'r')
import collections

N, K = map(int, input().split())
queue = collections.deque([N])
time = 0
flag = False
visit = [0] * 100001
while queue:

    for i in range(len(queue)):
        cur = queue.popleft()
        if cur == K:
            flag = True
            break

        nxts = [cur - 1, cur + 1, 2 * cur]
        for nxt in nxts:
            if 0 <= nxt <= 100000 and visit[nxt] is 0:
                visit[nxt] = 1
                queue.append(nxt)

    if flag is True:
        break
    time += 1

print(time)

# if flag is True:
#     print(time)
# else:
#     print(-1)
