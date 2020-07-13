from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def spread():
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                n = 0
                for adj in adj_list:
                    nxt1, nxt2 = i + adj[0], j + adj[1]
                    if 0 <= nxt1 < R and 0 <= nxt2 < C and board[nxt1][nxt2] != -1:
                        board2[nxt1][nxt2] += board[i][j] // 5
                        n += 1
                board2[i][j] += board[i][j] - (board[i][j] // 5) * n


def cleaning():
    for i in range(machine_top - 2, -1, -1):
        board2[i+1][0] = board2[i][0]

    for j in range(1, C):
        board2[0][j-1] = board2[0][j]

    for i in range(machine_top):
        board2[i][C-1] = board2[i+1][C-1]

    for j in range(C - 1, 1, -1):
        board2[machine_top][j] = board2[machine_top][j-1]
    board2[machine_top][1] = 0

    for i in range(machine_top + 2, R - 1):
        board2[i][0] = board2[i+1][0]

    for j in range(C - 1):
        board2[R-1][j] = board2[R-1][j+1]

    for i in range(R-1, machine_top + 1, -1):
        board2[i][C-1] = board2[i-1][C-1]

    for j in range(C-1, 1, -1):
        board2[machine_top+1][j] = board2[machine_top+1][j-1]
    board2[machine_top+1][1] = 0


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

machine_top = 0
for r in range(R):
    if board[r][0] == -1:
        machine_top = r
        break

adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dust = 0
for _ in range(T):

    board2 = [[0] * C for _ in range(R)]
    board2[machine_top][0] = board2[machine_top + 1][0] = -1

    spread()
    cleaning()

    board = [row[:] for row in board2]

for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            dust += board[r][c]

print(dust)
