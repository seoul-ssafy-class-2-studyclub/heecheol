# 플로이드 워샬 알고리즘

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    inf = float('inf')
    board = [[inf] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        board[a][b] = 1
        board[b][a] = 1

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if i != k:
                if board[i][k] < 2:
                    for j in range(1, N + 1):
                        if i != j and j != k:
                            board[i][j] = min(board[i][k] + board[k][j], board[i][j])

    cnt = 0
    for i in range(2, N + 1):
        if board[1][i] <= 2:
            cnt += 1

    print('#{} {}'.format(tc, cnt))