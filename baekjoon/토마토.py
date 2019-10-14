import collections
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())

box = [input().split() for _ in range(M)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = collections.deque()
for i in range(M):
    for j in range(N):
        if box[i][j] == '1':
            queue.append((i, j))

cnt = -1
while queue:
    queue2 = collections.deque()
    while queue:
        ix, iy = queue.popleft()
        for adj in adj_list:
            nxt1 = ix + adj[0]
            nxt2 = iy + adj[1]
            if 0 <= nxt1 < M and 0 <= nxt2 < N:
                if box[nxt1][nxt2] == '0':
                    box[nxt1][nxt2] = '1'
                    queue2.append((nxt1, nxt2))

    cnt += 1
    queue = queue2

flag = False
for i in range(M):
    for j in range(N):
        if box[i][j] == '0':
            flag = True
            break
    if flag is True:
        break

if flag is True:
    print(-1)
else:
    print(cnt)