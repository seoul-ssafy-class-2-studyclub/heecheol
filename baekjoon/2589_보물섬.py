import sys
sys.stdin = open('input.txt', 'r')


def bfs(ii, jj):
    board2 = [row[:] for row in board]
    cnt = 0
    queue = [(ii, jj, cnt)]
    while queue:
        idx1, idx2, cnt = queue.pop(0)
        if board2[idx1][idx2] == 'L':
            board2[idx1][idx2] = cnt
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if board2[nxt1][nxt2] == 'L':
                        queue.append((nxt1, nxt2, board2[idx1][idx2] + 1))
    return cnt


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            result.append(bfs(i, j))

print(max(result))
