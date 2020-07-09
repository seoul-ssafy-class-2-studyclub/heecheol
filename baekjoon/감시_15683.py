from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def mark_left(idx1, idx2):
    check = 0
    for nxt2 in range(idx2 - 1, -1, -1):
        if board[idx1][nxt2] == '0':
            board[idx1][nxt2] = '#'
            check += 1
        elif board[idx1][nxt2] == '6':
            return check
    return check


def mark_right(idx1, idx2):
    check = 0
    for nxt2 in range(idx2 + 1, M):
        if board[idx1][nxt2] == '0':
            board[idx1][nxt2] = '#'
            check += 1
        elif board[idx1][nxt2] == '6':
            return check
    return check


def mark_up(idx1, idx2):
    check = 0
    for nxt1 in range(idx1 - 1, -1, -1):
        if board[nxt1][idx2] == '0':
            board[nxt1][idx2] = '#'
            check += 1
        elif board[nxt1][idx2] == '6':
            return check
    return check


def mark_down(idx1, idx2):
    check = 0
    for nxt1 in range(idx1 + 1, N):
        if board[nxt1][idx2] == '0':
            board[nxt1][idx2] = '#'
            check += 1
        elif board[nxt1][idx2] == '6':
            return check
    return check


def check_blind_spot():
    spot = 0
    for r in range(N):
        spot += board[r].count('0')

    return spot


def permutation(k, n, arr):
    if k == n:
        directions.append(arr)
        return
    else:
        if cctv[k][2] == '2':
            for d in range(2):
                permutation(k+1, n, arr+[d])
        else:
            for d in range(4):
                permutation(k+1, n, arr+[d])


N, M = map(int, input().split())
board = [input().split() for _ in range(N)]

cctv = []
directions = []

for i in range(N):
    for j in range(M):
        if board[i][j] == '0' or board[i][j] == '6' or board[i][j] == '#':
            continue
        elif board[i][j] == '5':
            mark_up(i, j)
            mark_right(i, j)
            mark_down(i, j)
            mark_left(i, j)
        else:
            cctv.append([i, j, board[i][j]])

cnt = len(cctv)
spots = check_blind_spot()

result = spots

if cnt:
    permutation(0, cnt, [])
    board2 = [row[:] for row in board]
    for direction in directions:
        board = [row[:] for row in board2]
        unchecked = spots
        for i in range(cnt):
            if cctv[i][2] == '1':
                if direction[i] == 0:
                    unchecked -= mark_up(cctv[i][0], cctv[i][1])
                elif direction[i] == 1:
                    unchecked -= mark_right(cctv[i][0], cctv[i][1])
                elif direction[i] == 2:
                    unchecked -= mark_down(cctv[i][0], cctv[i][1])
                else:
                    unchecked -= mark_left(cctv[i][0], cctv[i][1])
            elif cctv[i][2] == '2':
                if direction[i] == 0:
                    unchecked -= mark_up(cctv[i][0], cctv[i][1]) + mark_down(cctv[i][0], cctv[i][1])
                else:
                    unchecked -= mark_right(cctv[i][0], cctv[i][1]) + mark_left(cctv[i][0], cctv[i][1])
            elif cctv[i][2] == '3':
                if direction[i] == 0:
                    unchecked -= mark_up(cctv[i][0], cctv[i][1]) + mark_right(cctv[i][0], cctv[i][1])
                elif direction[i] == 1:
                    unchecked -= mark_right(cctv[i][0], cctv[i][1]) + mark_down(cctv[i][0], cctv[i][1])
                elif direction[i] == 2:
                    unchecked -= mark_down(cctv[i][0], cctv[i][1]) + mark_left(cctv[i][0], cctv[i][1])
                else:
                    unchecked -= mark_left(cctv[i][0], cctv[i][1]) + mark_up(cctv[i][0], cctv[i][1])
            else:
                if direction[i] == 0:
                    unchecked -= mark_up(cctv[i][0], cctv[i][1]) + mark_right(cctv[i][0], cctv[i][1]) + mark_down(cctv[i][0], cctv[i][1])
                elif direction[i] == 1:
                    unchecked -= mark_right(cctv[i][0], cctv[i][1]) + mark_down(cctv[i][0], cctv[i][1]) + mark_left(cctv[i][0], cctv[i][1])
                elif direction[i] == 2:
                    unchecked -= mark_down(cctv[i][0], cctv[i][1]) + mark_left(cctv[i][0], cctv[i][1]) + mark_up(cctv[i][0], cctv[i][1])
                else:
                    unchecked -= mark_left(cctv[i][0], cctv[i][1]) + mark_up(cctv[i][0], cctv[i][1]) + mark_right(cctv[i][0], cctv[i][1])

        if unchecked < result:
            result = unchecked

print(result)
