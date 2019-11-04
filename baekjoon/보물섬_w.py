from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt', 'r')


def route(idx1, idx2):
    global hours
    x = y = 0
    queue = collections.deque()
    queue.append((idx1, idx2))
    visited[idx1][idx2] = True
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for adj in adj_list:
                nxt1, nxt2 = x + adj[0], y + adj[1]

                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if visited[nxt1][nxt2] is False and board[nxt1][nxt2] == 'L':
                        visited[nxt1][nxt2] = True
                        queue.append((nxt1, nxt2))
    # pprint(visited)
    queue.append((x, y))
    visited[x][y] = False
    board[x][y] = 'W'
    cnt = -1
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for adj in adj_list:
                nxt1, nxt2 = x + adj[0], y + adj[1]

                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if visited[nxt1][nxt2] is True and board[nxt1][nxt2] == 'L':
                        visited[nxt1][nxt2] = False
                        board[nxt1][nxt2] = 'W'
                        queue.append((nxt1, nxt2))
    if cnt > hours:
        hours = cnt
    # pprint(visited)


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
