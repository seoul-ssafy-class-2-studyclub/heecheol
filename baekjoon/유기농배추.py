import collections
import sys
sys.stdin = open('input.txt', 'r')


adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for tc in range(1, int(input()) + 1):
    M, N, K = map(int, input().split())

    board = [[0] * M for _ in range(N)]
    queue = collections.deque()

    for _ in range(K):
        c, r = map(int, input().split())
        board[r][c] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    if board[x][y] == 1:
                        board[x][y] = 0
                        for adj in adj_list:
                            nxt1 = x + adj[0]
                            nxt2 = y + adj[1]
                            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                                if board[nxt1][nxt2] == 1:
                                    queue.append((nxt1, nxt2))

    print(cnt)

