import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# heapq (garbage, near, idx1, idx2)
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
garbage = []

for i in range(N):
    for j in range(M):
        if board[i][j] == '.' or board[i][j] == 'n':
            continue
        if board[i][j] == 'g':
            for adj in adj_list:
                nxt1, nxt2 = i + adj[0], j + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if board[nxt1][nxt2] == '.':
                        board[nxt1][nxt2] = 'n'
            continue

        if board[i][j] == 'F':
            fi, fj = i, j
            board[i][j] = '.'
            continue
        if board[i][j] == 'S':
            si, sj = i, j
            continue

