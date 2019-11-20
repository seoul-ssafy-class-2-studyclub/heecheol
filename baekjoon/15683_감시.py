from pprint import pprint
import itertools
import sys
sys.stdin = open('input.txt', 'r')


def permutation(k, length, arr):
    if k == length:
        dirs.append(arr)

    else:
        if cctv[k] == 2:
            for d in range(2):
                permutation(k + 1, length, arr + [d])
        else:
            for d in range(4):
                permutation(k + 1, length, arr + [d])


def up(idx1, idx2):
    nxt1 = idx1 - 1
    while nxt1 >= 0:
        if board[nxt1][idx2] == 6:
            break
        elif board[nxt1][idx2] == 0:
            board[nxt1][idx2] = 7   # '#' 대신 7
        nxt1 -= 1


def down(idx1, idx2):
    nxt1 = idx1 + 1
    while nxt1 < N:
        if board[nxt1][idx2] == 6:
            break
        elif board[nxt1][idx2] == 0:
            board[nxt1][idx2] = 7
        nxt1 += 1


def right(idx1, idx2):
    nxt2 = idx2 + 1
    while nxt2 < M:
        if board[idx1][nxt2] == 6:
            break
        elif board[idx1][nxt2] == 0:
            board[idx1][nxt2] = 7
        nxt2 += 1


def left(idx1, idx2):
    nxt2 = idx2 - 1
    while nxt2 >= 0:
        if board[idx1][nxt2] == 6:
            break
        elif board[idx1][nxt2] == 0:
            board[idx1][nxt2] = 7
        nxt2 -= 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 or board[i][j] == 6:
            continue
        elif board[i][j] == 5:
            up(i, j)
            down(i, j)
            right(i, j)
            left(i, j)
        elif 0 < board[i][j] < 5:
            cctv.append((board[i][j], i, j))

result = 987654321
board2 = [row[:] for row in board]
dirs = []
# dirs = list(itertools.product(list(range(4)), repeat=len(cctv)))
permutation(0, len(cctv), [])

for dir in dirs:
    board = [row[:] for row in board2]
    for i in range(len(cctv)):
        num = cctv[i][0]
        if num == 1:
            if dir[i] == 0:
                up(cctv[i][1], cctv[i][2])
            elif dir[i] == 1:
                down(cctv[i][1], cctv[i][2])
            elif dir[i] == 2:
                right(cctv[i][1], cctv[i][2])
            else:
                left(cctv[i][1], cctv[i][2])
        elif num == 2:
            if dir[i] == 0:
                up(cctv[i][1], cctv[i][2])
                down(cctv[i][1], cctv[i][2])
            else:
                right(cctv[i][1], cctv[i][2])
                left(cctv[i][1], cctv[i][2])
        elif num == 3:
            if dir[i] == 0:
                up(cctv[i][1], cctv[i][2])
                right(cctv[i][1], cctv[i][2])
            elif dir[i] == 1:
                right(cctv[i][1], cctv[i][2])
                down(cctv[i][1], cctv[i][2])
            elif dir[i] == 2:
                down(cctv[i][1], cctv[i][2])
                left(cctv[i][1], cctv[i][2])
            else:
                left(cctv[i][1], cctv[i][2])
                up(cctv[i][1], cctv[i][2])
        else:
            if dir[i] == 0:
                up(cctv[i][1], cctv[i][2])
                right(cctv[i][1], cctv[i][2])
                down(cctv[i][1], cctv[i][2])
            elif dir[i] == 1:
                right(cctv[i][1], cctv[i][2])
                down(cctv[i][1], cctv[i][2])
                left(cctv[i][1], cctv[i][2])
            elif dir[i] == 2:
                down(cctv[i][1], cctv[i][2])
                left(cctv[i][1], cctv[i][2])
                up(cctv[i][1], cctv[i][2])
            else:
                left(cctv[i][1], cctv[i][2])
                up(cctv[i][1], cctv[i][2])
                right(cctv[i][1], cctv[i][2])

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    if cnt < result:
        # pprint(board)
        result = cnt

print(result)