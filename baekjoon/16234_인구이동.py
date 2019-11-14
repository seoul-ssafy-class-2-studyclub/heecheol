from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt', 'r')


def join(ii, jj, m):
    queue = collections.deque([(ii, jj)])
    pos = []
    val = []
    while queue:
        idx1, idx2 = queue.popleft()
        if visit[idx1][idx2] == 0:
            pos.append((idx1, idx2))
            val.append(board[idx1][idx2])
            visit[idx1][idx2] = m
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if visit[nxt1][nxt2] == 0 and L <= abs(board[idx1][idx2] - board[nxt1][nxt2]) <= R:
                        queue.append((nxt1, nxt2))

    # step2 => union
    if len(pos) > 1:
        avg = sum(val) // len(val)
        for r, c in pos:
            board[r][c] = avg


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
while True:
    # step1 => join
    visit = [[0] * N for _ in range(N)]

    mark = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                mark += 1
                join(i, j, mark)

    if mark == N * N:
        break

    cnt += 1

# pprint(board)
print(cnt)
