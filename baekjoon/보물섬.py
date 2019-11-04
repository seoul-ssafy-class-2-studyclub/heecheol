import collections
import sys
sys.stdin = open('input.txt', 'r')


def route(idx1, idx2):
    global hours
    visited2 = [row[:] for row in visited]
    queue = collections.deque()
    queue.append((idx1, idx2))
    visited2[idx1][idx2] = True
    cnt = -1
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for adj in adj_list:
                nxt1, nxt2 = x + adj[0], y + adj[1]

                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if board[nxt1][nxt2] == 'L' and visited2[nxt1][nxt2] is False:
                        visited2[nxt1][nxt2] = True
                        queue.append((nxt1, nxt2))

    if cnt > hours:
        hours = cnt


N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
hours = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            route(i, j)

print(hours)
